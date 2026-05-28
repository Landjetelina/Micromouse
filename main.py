import os
print(os.listdir())

from machine import Pin, PWM, ADC
import time
from Micromouse.lib.software.robot import Robot
from tests import *


# Ovdje pozvati primjer iz tests.py

if __name__ == "__main__":
    robot = Robot()

    samo_senzori(robot)