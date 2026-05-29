from machine import Pin, PWM, ADC
import time

#100 000 ne postoji — duty_u16 je 16-bitni, maksimum je 65535. Sve iznad toga se "wraparound" ili baca grešku, ne daje više brzine
def motori_naprijed(robot, snaga):
    robot.l_motor1.value(1)  
    robot.l_motor2.value(0)
    robot.r_motor1.value(0)
    robot.r_motor2.value(1)
    # NE MIJENJATI OVU VRIJEDNOST!
    robot.l_speed.duty_u16(int(snaga * 0.9)) # Malo usporiti da ide ravno (otprilike 0.9 ako su kotaci na istoj udaljenosti)
    robot.r_speed.duty_u16(int(snaga * 1)) 
    print(f"Brzina r: {robot.r_speed}, Brzina l: {robot.l_speed}")

def motori_stop(robot):
    robot.l_motor1.value(0)
    robot.l_motor1.value(0)
    
    robot.r_motor1.value(0)
    robot.r_motor2.value(0)
    
    robot.l_speed.duty_u16(0)
    robot.r_speed.duty_u16(0)