from motor import Motor
import time

m = Motor('moteur 1', 5, 3, 10)
m.start()
time.sleep(3)
m.reverse(True)
time.sleep(3)
m.reverse(True)
time.sleep(3)
m.stop()
m.clear()
