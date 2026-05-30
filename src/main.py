# import os
# print(f"Pico --> {os.listdir()}")
# print(f"lib/software: {os.listdir('./lib/software')}\n")

# import machine
# # machine.reset()

# import time
# from lib.software.robot import Robot
# import tests 


# # Ovdje pozvati primjer iz tests.py
# n, kanal, snaga = 50, 3, 65535
# duration, delay = 5, 0.05

# if __name__ == "__main__":
#     robot = Robot()
#     open("ocitanja.txt", "w").close()  # prazni datoteku
    
#     try:
#         for _ in range(int(duration / delay)):
#             cilj_pronađen = robot.navigiraj()
#             print(robot.ispisi_dist(datoteka=True))
#             time.sleep(delay)
#             if cilj_pronađen:
#                 break  # izlazi iz petlje
#     finally:
#         robot.motori_stop()

import os
print(f"Pico --> {os.listdir()}")
print(f"lib/software: {os.listdir('./lib/software')}\n")
import time
from lib.software.robot import Robot

duration, delay = 60, 0.05  # 60 sekundi da ima dovoljno vremena

if __name__ == "__main__":
    robot = Robot()
    open("ocitanja.txt", "w").close()

    try:
        koraci = 0
        for _ in range(int(duration / delay)):
            cilj, koraci = robot.navigiraj(koraci=koraci)
            time.sleep(delay)
            if cilj:
                break
    finally:
        robot.motori_stop()