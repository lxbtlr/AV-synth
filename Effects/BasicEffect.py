from selenium import webdriver
import time

# Give code for an empty class called BasicEffect
class BasicEffect:
    def __init__(self, debug=False):
        self.driver = webdriver.Firefox()
        self.debug = debug
        URL='http://127.0.0.1:8080'
        self.driver.get(URL)
        self.o1_osc = (10, .1, .1)
        self.o2_color = (1,1,1)

    def modOne(self, val):
        """
        Modification for parameters controlled by encoder one.

        Parameters:
            val (int): The delta of the encoder {-1, 1}
        """
        self.o1_osc += val
        if self.debug:
            print(self.o1_osc)

    def modTwo(self, val):
        """
        Modification for parameters controlled by encoder one.

        Parameters:
            val (int): The delta of the encoder {-1, 1}
        """
        prev_color = self.o2_color
        self.o2_color = (prev_color[0], prev_color[1], prev_color[2])
        if self.debug:
            print(self.o2_color)

    def applyEffect(self, val):
        """
        Apply effects and send the command to the gecko driver
        """
        scriptcmd = f"osc{self.o1_osc}.color({self.o2_color}).out(o1)\nrender(o1)"
        if self.debug:
            print(scriptcmd)
        self.driver.execute_script(scriptcmd)

