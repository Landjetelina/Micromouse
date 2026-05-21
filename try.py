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

# Motor driver
left_motor_1  = Pin(4, Pin.OUT)
left_motor_2  = Pin(5, Pin.OUT)
right_motor_1 = Pin(6, Pin.OUT)
right_motor_2 = Pin(7, Pin.OUT)

speed_left  = PWM(Pin(8))
speed_right = PWM(Pin(9))
speed_left.freq(1000)
speed_right.freq(1000)

PRAG = 30000  # podesi eksperimentalno (0-65535)

def mux_odaberi(kanal):
    # kanal 0-3 za 4 fototranzistora
    mux_s[0].value((kanal >> 0) & 1)
    mux_s[1].value((kanal >> 1) & 1)
    mux_s[2].value(0)  # treći bit = 0 za kanale 0-3

def citaj_senzor(kanal):
    mux_odaberi(kanal)
    time.sleep_us(50)  # kratka pauza da se MUX stabilizira
    return adc.read_u16()

#100 000 ne postoji — duty_u16 je 16-bitni, maksimum je 65535. Sve iznad toga se "wraparound" ili baca grešku, ne daje više brzine
def motori_naprijed(brzina=65535):
    left_motor_1.value(0)  
    left_motor_2.value(1)
      
    right_motor_1.value(1)
    right_motor_2.value(0)
    speed_left.duty_u16(brzina)
    speed_right.duty_u16(brzina)

def motori_stop():
    left_motor_1.value(0); left_motor_2.value(0)
    right_motor_1.value(0); right_motor_2.value(0)
    speed_left.duty_u16(0)
    speed_right.duty_u16(0)

# Upali sve IR LEDs
for led in ir_led:
    led.value(1)

while True:
    ocitanja = [citaj_senzor(k) for k in range(4)]
    prepreka = any(v > PRAG for v in ocitanja)

    print(f"Senzori: {ocitanja} | {'STOP' if prepreka else 'OK'}")

    if prepreka:
        motori_stop()
    else:
        motori_naprijed()

    time.sleep(0.05)