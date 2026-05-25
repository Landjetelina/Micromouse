from machine import Pin, PWM, ADC
import time

# IR LED kontrola (pali emitere)
ir_led = [
    Pin(0, Pin.OUT),  # IR_left
    Pin(1, Pin.OUT),  # IR_left-right
    Pin(2, Pin.OUT),  # IR_right-left
    Pin(3, Pin.OUT),  # IR_right
]

# MUX select (odabir kojeg fototranzistora čitaš)
mux_s = [
    Pin(16, Pin.OUT),  # MUX_foto_0
    Pin(17, Pin.OUT),  # MUX_foto_1
    Pin(18, Pin.OUT),  # MUX_foto_2
]

# ADC za čitanje MUX izlaza
adc = ADC(Pin(26))  # IRT_READ

PRAG = 4000  # podesi eksperimentalno (0-65535) - vrijednost iznad koje se smatra da je prepreka detektirana

def mux_odaberi(kanal):
    # kanal 0-3 za 4 fototranzistora
    mux_s[0].value((kanal >> 0) & 1)
    mux_s[1].value((kanal >> 1) & 1)
    mux_s[2].value((kanal >> 2) & 1) 

def citaj_senzor(kanal):
    mux_odaberi(kanal)
    time.sleep_us(50)           # kratka pauza da se MUX stabilizira
    return adc.read_u16()       # to je fototranz na gpio26, koji je povezan na MUX izlaz

# Upali sve IR LEDs
for led in ir_led:
    led.value(1)

while True:
    ocitanja = [citaj_senzor(k) for k in range(4)]
    prepreka = any(v > PRAG for v in ocitanja)

    print(f"Senzori: {ocitanja} | {'STOP' if prepreka else 'OK'}")

    if prepreka:
        print("Prepreka detektirana!")

    time.sleep(0.05) 