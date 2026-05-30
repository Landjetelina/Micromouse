from machine import Pin, PWM, ADC
import time
import lib.software.utility as utility
# from Micromouse.lib.software.robot import Robot

# Definirani svi primjeri testiranja, potrebno primjer pozvati iz main.py

PRAG = 5000

def hello_world():
    print("Pico kaže hello world! :)")

def motori_fwd(robot, brzina, PRAG=PRAG):
    # PRAG podesi eksperimentalno (0-65535) - vrijednost iznad koje se smatra da je prepreka detektirana

    while True:
        ocitanja = [robot.citaj_senzor(k) for k in range(4)]
        prepreka = any(v > PRAG for v in ocitanja)

        print(f"Senzori: {ocitanja} | {'STOP' if prepreka else 'OK'}")

        if prepreka:
            robot.motori_stop()
        else:
            robot.motori_naprijed(brzina)

        time.sleep(0.05)  

def jedan_senzor(robot, kanal, PRAG=PRAG):
    
    # Iz netliste
    # SAMO TU MIJENJAJ OVE VARIJABLE
    # kanal = 0–3, mijenjaj za testiranje
    # 0 = IR_left (Q9) 
    # 1 = IR_left-right (Q5) 
    # 2 = IR_right-left (Q6) 
    # 3 = IR_right (Q7) 

    
    # optimalno je držati prag 3000-4000
    # Upali samo IR LED za odabrani kanal
    robot.ir_led[kanal].value(1)
    robot.mux_odaberi(kanal)

    while True:
        # time.sleep_us(50)
        vrijednost = robot.adc.read_u16()
        prepreka = vrijednost > PRAG
        print(f"Kanal {kanal}: {vrijednost} | {'PREPREKA' if prepreka else 'OK'}")
        time.sleep(0.1)
        
    

def kalibriraj_senzor(robot, kanal, n=10):
    while True:
        mjerenje = utility.citaj_prosjek_n_mjeranja_senzora(robot, kanal, n=n)
        print(f"Senzor {kanal}: {mjerenje}")
        udalj = utility.dist_to_wall(mjerenje, kanal)
        print(f"Udaljenost do prepreke: {udalj}cm")
        time.sleep(0.25)

def ispisi_koord(robot):
    while True:
        koord_prepreka = robot.koord_svi_senzori()
        print("[" + ", ".join(
                "None" if prepreka is None else f"({prepreka[0]:.2f}, {prepreka[1]:.2f})"
                for prepreka in koord_prepreka) + "]")
        time.sleep(0.3)