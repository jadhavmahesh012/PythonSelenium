import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


serv_obj=Service("C:/Mahesh/chromedriver-win64/chromedriver.exe")
driver=webdriver.Chrome(service=serv_obj)

driver.get("https://demo.nopcommerce.com/")

driver.maximize_window()

elements=driver.find_elements(By.XPATH,"")



time.sleep(2)
driver.quit()