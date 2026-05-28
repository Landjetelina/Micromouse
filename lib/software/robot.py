from machine import Pin, PWM, ADC
import time

import Micromouse.lib.software.utility as utility, Micromouse.lib.software.izvedba as izvedba

class Robot:
    def __init__(self) -> None:

        SPEED_FREQ = 1000  # frekvencija PWM signala (1 kHz je dobar izbor za motore)

        # postavlja IR LED za OUT
        self.ir_led = utility.ir_led_ctrl(self)  

        # postavlja MUX za OUT
        self.mux_s = utility.mux_s_ctrl(self) 

        self.adc = ADC(Pin(26))  # IRT_READ, čita podatke s IR senzora
        
        # Motor driveri
        self.l_motor1, self.l_motor2 = Pin(4, Pin.OUT), Pin(5, Pin.OUT)
        self.r_motor1, self.r_motor2 = Pin(6, Pin.OUT), Pin(7, Pin.OUT)

        # Brzine motora
        self.l_speed, self.r_speed = PWM(Pin(8)), PWM(Pin(9))
        # prevelika frekvencija može uzrokovati pregrijavanje motora, a premala može uzrokovati zujanje i neefikasno upravljanje brzinom
        self.l_speed.freq(SPEED_FREQ)  
        self.r_speed.freq(SPEED_FREQ)  
        
    def mux_odaberi(self, kanal):
        # kanal 0-3 za 4 fototranzistora
        self.mux_s[0].value((kanal >> 0) & 1) # niži bit
        self.mux_s[1].value((kanal >> 1) & 1) # viši bit
        #self.mux_s[2].value((kanal >> 2) & 1)
    
    # Utility
    def citaj_senzor(self, kanal):
        return utility.citaj_senzor(self, kanal)
    def ir_led_ctrl(self):
        return utility.ir_led_ctrl(self)
    def mux_s_ctrl(self):
        return utility.mux_s_ctrl(self)
    
    # Izvedba
    #100 000 ne postoji — duty_u16 je 16-bitni, maksimum je 65535. Sve iznad toga se "wraparound" ili baca grešku, ne daje više brzine
    def motori_naprijed(self, brzina=45535):
        izvedba.motori_naprijed(self, brzina)
    def motori_stop(self):
        izvedba.motori_stop(self)
    

    
    