from evdev import InputDevice, categorize, ecodes
from rich.live import Live
from rich.table import Table
from pynput import keyboard
from selenium import webdriver
from Effects import *
import time
import evdev
import rich
import random

effect = BasicEffect()
EFFECTS={BasicEffect(), DemoEffectTwo()}

def shuffle_effect():
    """
    Shuffle the effect
    """
    global effect
    effect_new = EFFECTS-effect
    rand_num = random.randint(0, len(effect_new)-1)
    effect = effect_new[rand_num]

if __name__ == "__main__":
    global effect
    dial_1 = 50
    dial_2 = 50
    # Create a new instance of the Firefox driver
    clk_1 = 7
    dt_1 = 11
    press_1 = 13

    clk_2 = 7 # change later
    dt_2 = 16
    press_2 = 18

    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(clk_1, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    GPIO.setup(clk_2, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    GPIO.setup(dt_1, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    GPIO.setup(dt_2, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    GPIO.setup(press_1, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    GPIO.setup(press_2, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    GPIO.add_event_detect(press_1, GPIO.RISING, callback=effect.applyEffect, bouncetime=30)
    GPIO.add_event_detect(press_2, GPIO.RISING, callback=shuffle_effect, bouncetime=30)
    clk1LastState = GPIO.input(clk_1)
    clk2LastState = GPIO.input(clk_2)

    try:
        while True:
            clkState1 = GPIO.input(clk_1)
            dtState1 = GPIO.input(dt_1)
            if clkState1 != clk1LastState:
                if dtState1 != clkState1:
                    effect.modOne(1)
                else:
                    effect.modOne(-1)
                print counter
            clkLastState = clkState
            sleep(0.01)
    finally:
        GPIO.cleanup()

# def increment(val):
#     if val >= 100:
#         val = 100
#     else:
#         val += 1
#     return val
# 
# def decrement(val): 
#     if val <= 0:
#         val = 0
#     else:
#         val -= 1
#     return val
# 
# def generate_table(var1,var2) -> Table:
#     """Give us the state of our vars."""
#     table = Table()
#     table.add_column("Name")
#     table.add_column("Value")
#     
#     table.add_row(f"Dial 1",f"{var1}")
#     table.add_row(f"Dial 2",f"{var2}")
#     return table
# 
