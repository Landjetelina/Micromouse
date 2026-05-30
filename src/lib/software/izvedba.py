from machine import Pin, PWM, ADC
import time
# from robot import Robot


#100 000 ne postoji — duty_u16 je 16-bitni, maksimum je 65535. Sve iznad toga se "wraparound" ili baca grešku, ne daje više brzine
def motori_naprijed(robot, snaga):
    robot.l_motor1.value(1)  
    robot.l_motor2.value(0)
    robot.r_motor1.value(0)
    robot.r_motor2.value(1)
    # NE MIJENJATI OVU VRIJEDNOST!
    robot.l_speed.duty_u16(int(snaga * 0.9)) # Malo usporiti da ide ravno (otprilike 0.9 ako su kotaci na istoj udaljenosti)
    robot.r_speed.duty_u16(int(snaga * 1)) 
    # print(f"Brzina r: {robot.r_speed}, Brzina l: {robot.l_speed}")

def motori_stop(robot):
    robot.l_motor1.value(0)
    robot.l_motor2.value(0)
    
    robot.r_motor1.value(0)
    robot.r_motor2.value(0)
    
    robot.l_speed.duty_u16(0)
    robot.r_speed.duty_u16(0)

def skreni_ulijevo(robot):
    snaga = 65535
    dist = robot.ispisi_dist()

    # Greska ovdje!
    if not dist[0] and not dist[1] and dist[2] and dist[3]:
        robot.r_speed.duty_u16(int(snaga * 0.4)) 
    else:
        robot.r_speed.duty_u16(snaga) 

def motori_fwd_pid(robot):
    BASE_SPEED = 45000
    MAX_SPEED  = 65535
    PRAG = 4


    pid = robot.pid
    ocitanja = robot.ispisi_dist(datoteka=True)
    # ocitanja[0], ocitanja[1] = lijevo
    # ocitanja[2], ocitanja[3] = desno

    MAX_DIST = 20
    ocitanja = [o if o else MAX_DIST for o in ocitanja]

    lijevo = (ocitanja[0] + ocitanja[1]) / 2
    desno  = (ocitanja[2] + ocitanja[3]) / 2

    # # Provjera prepreke ispred
    # prepreka = any((o and o <= PRAG) for o in ocitanja)
    # if prepreka:
    #     robot.motori_stop()
    #     pid.reset()
    #     return

    # Greška: pozitivna = robot je bliže desnom zidu

    error = desno - lijevo
    korekcija = pid.compute(error)

    l_snaga = int(max(0, min(MAX_SPEED, BASE_SPEED - korekcija)))
    r_snaga = int(max(0, min(MAX_SPEED, BASE_SPEED + korekcija)))

    #robot.motori_naprijed() # vjerojatno se ove linije ispod mogu zamijeniti s ovom, ali nisam probao

    robot.l_motor1.value(1)
    robot.l_motor2.value(0)
    robot.r_motor1.value(0)
    robot.r_motor2.value(1)
    robot.l_speed.duty_u16(int(l_snaga * 0.9))
    robot.r_speed.duty_u16(int(r_snaga * 1.0))


