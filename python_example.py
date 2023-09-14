from selenium import webdriver
import time

# Create a new instance of the Firefox driver
driver = webdriver.Firefox()
URL='http://127.0.0.1:8080'
driver.get(URL)
driver.execute_script("hide()")
driver.execute_script("osc(10).out(o1)\nrender(o1)")
time.sleep(5)
driver.execute_script("osc(20).out(o1)\nrender(o1)")
