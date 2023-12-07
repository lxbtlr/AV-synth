from pynput import keyboard
from selenium import webdriver
import time
import sys
import threading
from Effects import *

eff3 = "noise(3,0.1,7).rotate(1,-1,-2).mask(shape(20)).colorama(0.5).modulateScale(o0).modulateScale(o0,1,).blend(o0).blend(o0).blend(o0).blend(o0).out(o0)"
eff1 = Eff1()
eff2 = Eff2()
eff3 = Eff3()
eff4 = Eff4()
eff5 = Eff5()
eff6 = Eff6()
eff7 = Eff7()
eff8 = Eff8()
eff9 = Eff9()
eff10 = Eff10()
eff11 = Eff11()
eff12 = Eff12()
eff13 = Eff13()
eff14 = Eff14()
eff15 = Eff15()
eff16 = Eff16()
eff17 = Eff17()
eff18 = Eff18()

currEffect = eff1
effects_p1 = {'c':eff1, 'f': eff2, 'i': eff9, 'b':eff3, 'e':eff4, 'h':eff5, 'a':eff6, 'd':eff7, 'g':eff8}
effects_p2 = {'c':eff10, 'f': eff11, 'i': eff12, 'b':eff13, 'e':eff14, 'h':eff15, 'a':eff16, 'd':eff17, 'g':eff18}
CHANGED = False
keypress_event = threading.Event()
effects = effects_p1

def on_press(key):
    global currEffect
    global effects
    print('pressed')
    try:
        pressed = key.char.strip()
        if pressed == '1':
            keypress_event.set()
            print('Decrement dial 1')
            currEffect.modOne(-1)
        elif pressed == '3':
            keypress_event.set()
            print('Increment dial 1')
            currEffect.modOne(1)
        elif pressed == '4':
            keypress_event.set()
            print('Decrement dial 2')
            currEffect.modTwo(-1)
        elif pressed == '6':
            keypress_event.set()
            print('Increment dial 2')
            currEffect.modTwo(1)
        elif pressed == '9':
            keypress_event.set()
            print('Decrement dial 3')
            currEffect.modThree(-1)
        elif pressed == '7':
            keypress_event.set()
            print('Increment dial 3')
            currEffect.modThree(1)
        elif pressed == '2':
            effects = effects_p1
        elif pressed == '5':
            effects = effects_p2
        elif pressed in effects:
            keypress_event.set()
            print('Switch!')
            currEffect = effects[pressed]
    except AttributeError:
        pass

def increment(val):
    if val >= 100:
        val = 100
    else:
        val += 1
    return val

def decrement(val): 
    if val <= 0:
        val = 0
    else:
        val -= 1
        return val

if __name__ == "__main__":
    # Create a new instance of the Firefox driver
    driver = webdriver.Firefox()
    URL='http://127.0.0.1:8080'
    driver.get(URL)
    # driver.execute_script("hide()")
    time.sleep(1)
    # driver.execute_script(currEffect.getFinalCommand())
    driver.execute_script(currEffect.getFinalCommand())
    listener = keyboard.Listener(on_press=on_press) 
    listener.start()
    keypress_event.clear()
    while True:
        # Display the current value of the variable
        keypress_event.wait()
        print('changing to {ind}')
        driver.execute_script(currEffect.getFinalCommand())
        print(currEffect.getFinalCommand())
        keypress_event.clear()
    listener.join()


