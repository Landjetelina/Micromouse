from machine import Pin, PWM, ADC
import time
import lib.software.konstante as konst
import math

def mux_odaberi(robot, kanal):
        # kanal 0-3 za 4 fototranzistora
        robot.mux_s[0].value((kanal >> 0) & 1) # niži bit
        robot.mux_s[1].value((kanal >> 1) & 1) # viši bit
        #self.mux_s[2].value((kanal >> 2) & 1)
    
def citaj_senzor(robot, kanal):
    robot.mux_odaberi(kanal)
    time.sleep_us(50)                # kratka pauza da se MUX stabilizira
    return robot.adc.read_u16()       # to je fototranz na gpio26, koji je povezan na MUX izlaz

# IR LED kontrola (pali emitere)
def ir_led_ctrl():
    ir_led = [
        Pin(0, Pin.OUT),  # IR_left
        Pin(1, Pin.OUT),  # IR_left-right
        Pin(2, Pin.OUT),  # IR_right-left
        Pin(3, Pin.OUT)  # IR_right
    ]
    # pali sve IR LEDs
    for led in ir_led:
        led.value(1)
    return ir_led

# MUX select (odabir kojeg fototranzistora čitaš)
def mux_s_ctrl():
    mux_s = [
        Pin(16, Pin.OUT),  # MUX_foto_0
        Pin(17, Pin.OUT),  # MUX_foto_1
        Pin(18, Pin.OUT)]  # MUX_foto_2
    return mux_s

def citaj_prosjek_n_mjeranja_senzora(robot, kanal, n=10):
    suma = 0
    for _ in range(n):
        suma += robot.citaj_senzor(kanal) 
        time.sleep_us(50) 
    return suma / n               


# Vraća udaljenost u cm koju mjeri senzor do zida
def dist_to_wall(mjerenje, kanal):
    values_list = konst.lookup_table[kanal]
    
    # Zid je bliže od 1.5cm
    if mjerenje > values_list[0][0]:
        return 1.5
    # Zid je dalje od 5cm
    if mjerenje < values_list[-1][0]:
        return None  # nema zida u blizini
    
    for i in range(len(values_list)-1): # zadnjeg ne treba provjeravati
        signal1, _ = values_list[i]
        signal2, udalj2 = values_list[i+1]
        if mjerenje <= signal1 and mjerenje > signal2:
            return udalj2
        
    raise Exception("Mjerni signal nije u rasponu! Ne može se pretvoriti u cm")

def dist_to_coord(mjerenja):
    print("mjerenja: ", mjerenja)
    rezultat = []
    for i in range(len(mjerenja)):
        if not mjerenja[i]:
            rezultat.append(None)
        else:
            rezultat.append((   # (x, y)
                (konst.d_cntr_trans[i] + mjerenja[i]) * math.sin(konst.alpha[i]),  # x
                (konst.d_cntr_trans[i] + mjerenja[i]) * math.cos(konst.alpha[i]),  # y
            ))
    if rezultat[1]:
        rezultat[1] = (rezultat[1][0], rezultat[1][1] - 2)  # senzor 1 nije dobro postavljen ova linija računa offset!
    return rezultat

def koord_svi_senzori(robot):
    mjerenja = [robot.dist_to_wall(robot.citaj_senzor(k), k) for k in range(4)]
    koord_prepreka = dist_to_coord(mjerenja)
    return koord_prepreka 

def ispisi_dist(robot):
    ocitanja = [robot.dist_to_wall(robot.citaj_senzor(k), k) for k in range(4)]
    print(f"Senzori: {ocitanja}cm")
    return ocitanja   

