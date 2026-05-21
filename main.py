from machine import ADC
import time
from test import *



sensor = ADC(26)

while True:
    print(sensor.read_u16())
    time.sleep(0.1)

# test()