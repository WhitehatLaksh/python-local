
import unittest
import time
import os
from selenium import webdriver
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
driver = webdriver.Chrome(options=options)


#class FirstSampleTest(unittest.TestCase):
    # Generate capabilites from here: https://www.lambdatest.com/capabilities-generator/
    # setUp runs before each test case and
 ##      desired_caps = {
   #         'LT:Options': {
    #            "build": "Python Demo",  # Change your build name here
     #           "name": "Python Demo Test",  # Change your test name here
      #          "platformName": "Windows 11",
       #         "selenium_version": "4.0.0",
        #        "console": 'true',  # Enable or disable console logs
         #       "network": 'true',  # Enable or disable network logs
              
          #  "browserName": "firefox",
           # "browserVersion": "latest",
        #}



def tearDown(self):
        self.driver.quit()

def test_demo_site(self):

       
        print('Loading URL')
        driver.get("https://www.google.com")

   #     driver.find_element(By.CLASS_NAME, "nav-action-inner" ).click()
   #     driver.find_element(By.ID, "Email").sendkeys("lakshayindian19@live.com")
           

if __name__ == "__main__":
    unittest.main()
