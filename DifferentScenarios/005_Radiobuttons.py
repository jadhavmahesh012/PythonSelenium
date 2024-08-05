import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

serv_obj=Service("C:/Mahesh/chromedriver-win64/chromedriver.exe")
driver=webdriver.Chrome(service=serv_obj)

driver.get("https://artoftesting.com/samplesiteforselenium")
driver.maximize_window()

Malebutton=driver.find_element(By.ID,"male")
Femalebutton=driver.find_element(By.ID,"female")
print("Validate visibility of Male radio button before click:",Malebutton.is_displayed())
print("Validate visibility of Female radio button before click:",Femalebutton.is_displayed())

Malebutton.click()
Femalebutton.click()
print("Validate Male radio button after click:",Malebutton.is_selected())
print("Validate Female radio button after click:",Femalebutton.is_selected())

print("Validate Male radio button after click:",Malebutton.is_enabled())
print("Validate Female radio button after click:",Femalebutton.is_enabled())

time.sleep(5)

driver.close()

