from machine import Pin, PWM, ADC
import time

#100 000 ne postoji — duty_u16 je 16-bitni, maksimum je 65535. Sve iznad toga se "wraparound" ili baca grešku, ne daje više brzine
def motori_naprijed(self, brzina=45535):
    self.l_motor1.value(1)  
    self.l_motor2.value(0)
    self.r_motor1.value(0)
    self.r_motor2.value(1)
    self.l_speed.duty_u16(int(brzina * 1)) 
    self.r_speed.duty_u16(int(brzina * 1.015)) #Treba biti mrvu brži da bi išao ravno

def motori_stop(self):
    self.l_motor1.value(0)
    self.l_motor1.value(0)
    
    self.r_motor1.value(0)
    self.r_motor2.value(0)
    
    self.l_speed.duty_u16(0)
    self.r_speed.duty_u16(0)