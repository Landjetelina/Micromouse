# from machine import Pin, PWM, ADC
# import time
# # from robot import Robot

# #100 000 ne postoji — duty_u16 je 16-bitni, maksimum je 65535. Sve iznad toga se "wraparound" ili baca grešku, ne daje više brzine
# def motori_naprijed(robot, snaga):
#     robot.l_motor1.value(1)  
#     robot.l_motor2.value(0)
#     robot.r_motor1.value(0)
#     robot.r_motor2.value(1)
#     # NE MIJENJATI OVU VRIJEDNOST!
#     robot.l_speed.duty_u16(int(snaga * 0.9)) # Malo usporiti da ide ravno (otprilike 0.9 ako su kotaci na istoj udaljenosti)
#     robot.r_speed.duty_u16(int(snaga * 1)) 
#     # print(f"Brzina r: {robot.r_speed}, Brzina l: {robot.l_speed}")

# def motori_stop(robot):
#     robot.l_motor1.value(0)
#     robot.l_motor2.value(0)
    
#     robot.r_motor1.value(0)
#     robot.r_motor2.value(0)
    
#     robot.l_speed.duty_u16(0)
#     robot.r_speed.duty_u16(0)

# PRAG = 7  # cm

# def navigiraj(robot, snaga=65535):
#     motori_stop(robot)
#     dist = robot.ispisi_dist()

#     if je_li_cilj(dist):
#         print("CILJ PRONAĐEN!")
#         return True  # signalizira main.py da sta
    
#     # dist[0] = lijevo, dist[1] = lijevo-naprijed
#     # dist[2] = desno,  dist[3] = desno-naprijed
    
#     left_open  = dist[0] is None or dist[0] > PRAG
#     front_open = dist[1] is None or dist[1] > PRAG
#     right_open = dist[2] is None or dist[2] > PRAG

#     if left_open:
#         _okreni_ulijevo_na_mjestu(robot, snaga)
#     elif front_open:
#         _idi_ravno(robot, snaga)
#     elif right_open:
#         _okreni_udesno_na_mjestu(robot, snaga)
#     else:
#         _okreni_nazad(robot, snaga)

# def _idi_ravno(robot, snaga):
#     robot.l_motor1.value(1)
#     robot.l_motor2.value(0)
#     robot.r_motor1.value(0)
#     robot.r_motor2.value(1)
#     robot.l_speed.duty_u16(int(snaga * 0.9))
#     robot.r_speed.duty_u16(snaga)

# def _okreni_ulijevo_na_mjestu(robot, snaga):
#     # Lijevi motor nazad, desni naprijed — okreće se na mjestu
#     robot.l_motor1.value(0)
#     robot.l_motor2.value(1)  # lijevi NAZAD
#     robot.r_motor1.value(0)
#     robot.r_motor2.value(1)  # desni NAPRIJED
#     robot.l_speed.duty_u16(int(snaga * 0.7))
#     robot.r_speed.duty_u16(int(snaga * 0.7))
#     time.sleep(0.3)  # prilagodi ovo dok ne okrene točno 90°

# def _okreni_udesno_na_mjestu(robot, snaga):
#     # Lijevi naprijed, desni motor nazad — okreće se na mjestu
#     robot.l_motor1.value(1)
#     robot.l_motor2.value(0)  # lijevi NAPRIJED
#     robot.r_motor1.value(1)
#     robot.r_motor2.value(0)  # desni NAZAD
#     robot.l_speed.duty_u16(int(snaga * 0.7))
#     robot.r_speed.duty_u16(int(snaga * 0.7))
#     time.sleep(0.3)  # prilagodi ovo dok ne okrene točno 90°

# def _okreni_nazad(robot, snaga):
#     # Dva puta desno = 180°
#     _okreni_udesno_na_mjestu(robot, snaga)
#     _okreni_udesno_na_mjestu(robot, snaga)

# def je_li_cilj(dist):
#     # Centar je 2x2 polje — nema zidova na barem 3 strane
#     otvoreno = sum(1 for d in dist if d is None or d > PRAG)
#     return otvoreno >= 3

from machine import Pin, PWM, ADC
import time

PRAG = 7  # cm — prilagodi nakon testiranja

def motori_naprijed(robot, snaga):
    robot.l_motor1.value(1)  
    robot.l_motor2.value(0)
    robot.r_motor1.value(0)
    robot.r_motor2.value(1)
    robot.l_speed.duty_u16(int(snaga * 0.9))
    robot.r_speed.duty_u16(int(snaga * 1))

def motori_stop(robot):
    robot.l_motor1.value(0)
    robot.l_motor2.value(0)
    robot.r_motor1.value(0)
    robot.r_motor2.value(0)
    robot.l_speed.duty_u16(0)
    robot.r_speed.duty_u16(0)

def navigiraj(robot, snaga=65535, koraci=0):
    motori_stop(robot)
    dist = robot.ispisi_dist()

    # dist[0] = lijevo, dist[1] = naprijed
    # dist[2] = desno,  dist[3] = desno-naprijed (ne koristimo za odluke)
    
    front_open = dist[1] is None or dist[1] > PRAG
    left_open  = dist[0] is None or dist[0] > PRAG
    right_open = dist[2] is None or dist[2] > PRAG

    # Provjera cilja — tek nakon što uđemo u labirint (koraci > 20)
    # Cilj = 2x2 polje = nema zida ni lijevo ni desno ni naprijed
    if koraci > 20 and front_open and left_open and right_open:
        print("CILJ PRONAĐEN!")
        return True, koraci

    # Nema prepreke naprijed — idi ravno
    if front_open:
        _idi_ravno(robot, snaga)

    # Prepreka naprijed — odluči kamo skrenuti
    elif left_open:
        _okreni_ulijevo(robot, snaga)

    elif right_open:
        _okreni_udesno(robot, snaga)

    # Zatvoreno sa svih strana — okreni se 180°
    else:
        _okreni_180(robot, snaga)

    return False, koraci + 1

# ─── Kretanje ────────────────────────────────────────────

def _idi_ravno(robot, snaga):
    robot.l_motor1.value(1)
    robot.l_motor2.value(0)
    robot.r_motor1.value(0)
    robot.r_motor2.value(1)
    robot.l_speed.duty_u16(int(snaga * 0.9))
    robot.r_speed.duty_u16(snaga)

def _okreni_ulijevo(robot, snaga):
    # Lijevi motor nazad, desni naprijed = okreće se na mjestu
    robot.r_motor1.value(0)
    robot.r_motor2.value(1)
    robot.l_motor1.value(0)
    robot.l_motor2.value(1)
    robot.r_speed.duty_u16(int(snaga * 0.7))
    robot.l_speed.duty_u16(int(snaga * 0.7))
    time.sleep(0.3)  # prilagodi dok ne bude točno 90°

def _okreni_udesno(robot, snaga):
    # Lijevi naprijed, desni motor nazad = okreće se na mjestu
    robot.r_motor1.value(1)
    robot.r_motor2.value(0)
    robot.l_motor1.value(1)
    robot.l_motor2.value(0)
    robot.r_speed.duty_u16(int(snaga * 0.7))
    robot.l_speed.duty_u16(int(snaga * 0.7))
    time.sleep(0.3)  # prilagodi dok ne bude točno 90°

def _okreni_180(robot, snaga):
    # Dva puta desno = 180°
    _okreni_udesno(robot, snaga)
    time.sleep(0.1)  # kratka pauza između
    _okreni_udesno(robot, snaga)