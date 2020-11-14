from pynput.mouse import Button, Controller

mouse = Controller()
import time
import os

def movimentar_mouse():
    troca = True
    while (True):
        mouse.position = (800, 300)
        if(troca):
            mouse.move(-20, 0)
            mouse.scroll(0, -1)
        else:
            mouse.move(40, 0)
            mouse.scroll(0, 1)
        time.sleep(3)
        troca = not troca

movimentar_mouse()
