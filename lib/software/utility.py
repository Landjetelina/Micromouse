from machine import Pin, PWM, ADC
import time



def mux_odaberi(self, kanal):
        # kanal 0-3 za 4 fototranzistora
        self.mux_s[0].value((kanal >> 0) & 1) # niži bit
        self.mux_s[1].value((kanal >> 1) & 1) # viši bit
        #self.mux_s[2].value((kanal >> 2) & 1)
    
def citaj_senzor(self, kanal):
    self.mux_odaberi(kanal)
    time.sleep_us(50)           # kratka pauza da se MUX stabilizira
    return self.adc.read_u16()       # to je fototranz na gpio26, koji je povezan na MUX izlaz

# IR LED kontrola (pali emitere)
def ir_led_ctrl(self):
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
def mux_s_ctrl(self):
    mux_s = [
        Pin(16, Pin.OUT),  # MUX_foto_0
        Pin(17, Pin.OUT),  # MUX_foto_1
        Pin(18, Pin.OUT)]  # MUX_foto_2
    return mux_s
    