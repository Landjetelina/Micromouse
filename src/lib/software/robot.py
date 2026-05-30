from machine import Pin, PWM, ADC
import time

import lib.software.utility as utility
import lib.software.izvedba as izvedba

class Robot:
    def __init__(self) -> None:

        SPEED_FREQ = 1000  # frekvencija PWM signala (1 kHz je dobar izbor za motore)
        

        # postavlja IR LED za OUT
        self.ir_led = utility.ir_led_ctrl()  

        # postavlja MUX za OUT
        self.mux_s = utility.mux_s_ctrl() 

        self.adc = ADC(Pin(26))  # IRT_READ, čita podatke s IR senzora
        
        # Motor driveri
        self.l_motor1, self.l_motor2 = Pin(4, Pin.OUT), Pin(5, Pin.OUT)
        self.r_motor1, self.r_motor2 = Pin(6, Pin.OUT), Pin(7, Pin.OUT)

        # Brzine motora
        self.l_speed, self.r_speed = PWM(Pin(8)), PWM(Pin(9))
        # prevelika frekvencija može uzrokovati pregrijavanje motora, a premala može uzrokovati zujanje i neefikasno upravljanje brzinom
        self.l_speed.freq(SPEED_FREQ)  
        self.r_speed.freq(SPEED_FREQ)  

    # Utility
    def mux_odaberi(self, kanal):
        utility.mux_odaberi(self, kanal)

    def citaj_senzor(self, kanal):
        return utility.citaj_senzor(self, kanal)

    def ir_led_ctrl(self):
        return utility.ir_led_ctrl()

    def mux_s_ctrl(self):
        return utility.mux_s_ctrl()

    def citaj_prosjek_n_mjeranja_senzora(self, kanal, n=10):
        return utility.citaj_prosjek_n_mjeranja_senzora(self, kanal, n)

    def dist_to_wall(self, mjerenje, kanal):
        return utility.dist_to_wall(mjerenje, kanal)
    
    def dist_to_coord(self, mjerenja):
        return utility.dist_to_coord(mjerenja)
    
    def koord_svi_senzori(self):
        return utility.koord_svi_senzori(self)
    
    def ispisi_dist(self):
        return utility.ispisi_dist(self)
 
    
    # Izvedba
    def motori_naprijed(self, snaga=65535):
        izvedba.motori_naprijed(self, snaga)

    def motori_stop(self):
        izvedba.motori_stop(self)
    

    
    