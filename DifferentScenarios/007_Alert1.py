import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common import by
from selenium.webdriver.common.by import By

serv_obj=Service("C:/Mahesh/chromedriver-win64/chromedriver.exe")
driver=webdriver.Chrome(service=serv_obj)

driver.get("https://the-internet.herokuapp.com/javascript_alerts")
driver.maximize_window()

driver.find_element(By.XPATH,"//button[normalize-space()='Click for JS Prompt']").click()
time.sleep(5)

alertwindow=driver.switch_to.alert

print("Text on alert windoww is:" +alertwindow.text)

alertwindow.send_keys("Mahesh")
time.sleep(5)
alertwindow.accept()
#alertwindow.dismiss()

driver.close()
#driver.quit()






