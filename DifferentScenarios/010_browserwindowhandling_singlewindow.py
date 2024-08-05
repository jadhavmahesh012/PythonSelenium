import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common import by
from selenium.webdriver.common.by import By

serv_obj=Service("C:/Mahesh/chromedriver-win64/chromedriver.exe")
driver=webdriver.Chrome(service=serv_obj)

'''switch_to.window(WindowID)
current_window_handle --Return windowID of single browser window
window_handle --Return windowID's of multiple browser window'''

driver.get("https://opensource-demo.orangehrmlive.com/")
driver.maximize_window()

currentwindowID=driver.current_window_handle
print("Current window ID is:"+currentwindowID)      #changing every time

time.sleep(5)
driver.find_element(By.XPATH,"//a[normalize-space()='OrangeHRM, Inc']").click()


time.sleep(5)
driver.close()