from evdev import InputDevice, categorize, ecodes
import evdev
import rich
from rich.live import Live
from rich.table import Table
from pynput import keyboard
from selenium import webdriver
import time


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

def generate_table(var1,var2) -> Table:
    """Give us the state of our vars."""
    table = Table()
    table.add_column("Name")
    table.add_column("Value")
    
    table.add_row(f"Dial 1",f"{var1}")
    table.add_row(f"Dial 2",f"{var2}")
    return table


if __name__ == "__main__":
    dial_1 = 50
    dial_2 = 50
    # Create a new instance of the Firefox driver
    driver = webdriver.Firefox()
    URL='http://127.0.0.1:8080'
    driver.get(URL)
    # driver.execute_script("hide()")
    driver.execute_script("osc(10).out(o1)\nrender(o1)")
    time.sleep(1)
    # driver.execute_script("vornoi(5,1,.3).out(o0)")
    # driver.execute_script("osc(20).out(o1)\nrender(o1)")
    driver.execute_script("osc(6, 0, 0.8) .color(1.14, 0.6,.80).rotate(0.92, 0.3).pixelate(20, 10).mult(osc(40, 0.03).thresh(0.4).rotate(0, -0.02)).modulateRotate(osc(20, 0).thresh(0.3, 0.6), () => 0.1 + mouse.x * 0.002).out(o0)")
    live = Live(generate_table(dial_1,dial_2), refresh_per_second=4)
    device = evdev.InputDevice('/dev/input/event0')
    
    with Live(generate_table(dial_1,dial_2), refresh_per_second=4) as live:  # update 4 times a second to feel fluid
        for event in device.read_loop():
            if event.type == evdev.ecodes.EV_KEY:
                key_event = categorize(event)
                
                if key_event.keystate == key_event.key_down:
                    if key_event.keycode == 'KEY_F':
                        # Increment the variable when 'a' is pressed 
                        dial_1 = decrement(dial_1)
                    elif key_event.keycode == 'KEY_J':
                        # Decrement the variable when 'd' is pressed 
                        dial_1 = increment(dial_1)
                    

                    final_script = f"osc({dial_1/10}, 0, 0.8) .color(1.14, 0.6,.80).rotate(0.92, 0.3).pixelate(20, 10).mult(osc({dial_2}, 0.03).thresh(0.4).rotate(0, -0.02)).modulateRotate(osc(20, 0).thresh(0.3, 0.6), () => 0.1 + mouse.x * 0.002).out(o0)"
                    live.console.print(f"{final_script}")
                    # Display the current value of the variable
                    live.update(generate_table(dial_1, dial_2))
                    driver.execute_script(f"osc({dial_1/10}, 0, 0.8) .color(1.14, 0.6,.80).rotate(0.92, 0.3).pixelate(20, 10).mult(osc({dial_2}, 0.03).thresh(0.4).rotate(0, -0.02)).modulateRotate(osc(20, 0).thresh(0.3, 0.6), () => 0.1 + mouse.x * 0.002).out(o0)")



