
import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common import by
from selenium.webdriver.common.by import By

serv_obj=Service("C:/Mahesh/chromedriver-win64/chromedriver.exe")
driver=webdriver.Chrome(service=serv_obj)

driver.get("https://demo.automationtesting.in/Frames.html")
driver.maximize_window()

driver.find_element(By.XPATH,"//a[normalize-space()='Iframe with in an Iframe']").click()

outerframe=driver.find_element(By.XPATH,"//iframe[@src='MultipleFrames.html']")
driver.switch_to.frame(outerframe)

innerframe=driver.find_element(By.XPATH,"/html[1]/body[1]/section[1]/div[1]/div[1]/iframe[1]")
driver.switch_to.frame(innerframe)

searchbox=driver.find_element(By.XPATH,"//input[@type='text']")

searchbox.send_keys("abc")
time.sleep(3)

searchbox.clear()
time.sleep(3)

searchbox.send_keys("Mahesh Jadhav")
time.sleep(3)

driver.close()





