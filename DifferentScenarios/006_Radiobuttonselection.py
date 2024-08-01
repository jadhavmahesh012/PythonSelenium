import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


serv_obj=Service("C:\Mahesh\chromedriver-win64\chromedriver.exe")
driver=webdriver.Chrome(service=serv_obj)

driver.get("https://artoftesting.com/samplesiteforselenium")
driver.maximize_window()

Malebutton=driver.find_element(By.ID,"male")
Femalebutton=driver.find_element(By.ID,"female")


Malebutton.click()
time.sleep(5)

Femalebutton.click()

if (Femalebutton.is_selected()):
    driver.save_screenshot("../Screenshots/FemaleRadiobutton.png")


driver.close()