import os

import machine
# machine.reset()

import time
from lib.software.robot import Robot
import tests 


# Ovdje pozvati primjer iz tests.py

if __name__ == "__main__":
    robot = Robot()
    n, kanal, snaga = 50, 3, 65535
    while True:
        robot.ispisi_dist()
        time.sleep(0.3)

