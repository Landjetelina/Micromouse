from machine import Pin, ADC
import time

# Iz netliste: MUX select pinovi
mux_s = [
    Pin(16, Pin.OUT),  # MUX_foto_0 → GPIO16
    Pin(17, Pin.OUT),  # MUX_foto_1 → GPIO17
    Pin(18, Pin.OUT),  # MUX_foto_2 → GPIO18
]

# IR LED za kanal koji testiraš
# kanal 0 → IR_left (GPIO0), kanal 1 → IR_left-right (GPIO1), itd.
IR_LEDS = [
    Pin(0, Pin.OUT),   # IR_left
    Pin(1, Pin.OUT),   # IR_left-right
    Pin(2, Pin.OUT),   # IR_right-left
    Pin(3, Pin.OUT),   # IR_right
]

# ADC: IRT_READ → GPIO26
adc = ADC(Pin(26))

# SAMO TU MIJENJAJ OVE VARIJABLE
KANAL = 3   # 0–3, mijenjaj za testiranje
# 0 = IR_left (Q9) radi
# 1 = IR_left-right (Q5) radi
# 2 = IR_right-left (Q6) radi
# 3 = IR_right (Q7) radi
PRAG = 4000

def mux_odaberi(kanal):
    mux_s[0].value((kanal >> 0) & 1)
    mux_s[1].value((kanal >> 1) & 1)
    mux_s[2].value((kanal >> 2) & 1)


# optimalno je držati prag 3000-4000
# Upali samo IR LED za odabrani kanal
IR_LEDS[KANAL].value(1)
mux_odaberi(KANAL)

while True:
    time.sleep_us(50)
    vrijednost = adc.read_u16()
    prepreka = vrijednost > PRAG
    print(f"Kanal {KANAL}: {vrijednost} | {'PREPREKA' if prepreka else 'OK'}")
    time.sleep(0.1)