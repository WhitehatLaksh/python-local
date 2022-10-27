from unittest import TestCase
from webbrowser import Chrome
from selenium import webdriver 
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By



driver = webdriver.Chrome(r"C:/Users/saini/OneDrive/Documents/project1/chromedriver.exe")

options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
driver = webdriver.Chrome(options=options)
driver.maximize_window()  
driver.maximize_window() 

    
if __name__ == '__main__': TestCase()


driver.get("https://unicreds.com/contact-us")  
time.sleep(100)
#driver.find_element_by_xpath('"//*[@id="exit_popup_close"]').click()
time.sleep(100)
#driver.find_element_by_xpath('//*[@id="zsiq_float"]/img').click()
time.sleep(10000)

