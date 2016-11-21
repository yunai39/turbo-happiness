# from motor import Motor
# from charriot import Chariot
import time
from getch import getch, pause

# m1 = Motor('moteur 1', 5, 3, 10)
# m2 = Motor('moteur 1', 5, 3, 10)
#
# charriot = Chariot(m1,m2)

"""
    Controle principal
"""


while True:
    z = getch()
    print(ord(z))
    time.sleep(1)