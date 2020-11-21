from ax import Ax12
import time
servo = Ax12()
counter = 0
while counter <= 1:
    for position in range(0,1023):
        try:
            servo.move(1,position)
        except Ax12.timeoutError:
            pass
        time.sleep(0.005)
    for position in range(1023,0, -1):
        try:
            servo.move(1,position)
        except Ax12.timeoutError:
            pass
        time.sleep(0.005)
    counter += 1