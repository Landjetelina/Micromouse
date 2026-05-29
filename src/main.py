import os
print(os.listdir())

import machine
# machine.reset()

import time
from lib.software.robot import Robot
import tests 


# Ovdje pozvati primjer iz tests.py

if __name__ == "__main__":
    robot = Robot()
    n, kanal, snaga = 50, 1, 65535
    tests.kalibriraj_senzor(robot, kanal, n)
