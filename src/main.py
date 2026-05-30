import os
print(f"Pico --> {os.listdir()}")
print(f"lib/software: {os.listdir('./lib/software')}\n")

import machine
# machine.reset()

import time
from lib.software.robot import Robot
import tests 


# Ovdje pozvati primjer iz tests.py

if __name__ == "__main__":
    robot = Robot()
    n, kanal, snaga = 50, 3, 65535
    duration, delay = 5, 0.05
    open("ocitanja.txt", "w").close()  # prazni datoteku
    
    for _ in range(int(duration / delay)):
        tests.motori_fwd(robot)
        robot.skreni_ulijevo()
        print(robot.ispisi_dist(datoteka=True))
        time.sleep(delay)
    
