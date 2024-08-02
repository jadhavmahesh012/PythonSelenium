import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common import by
from selenium.webdriver.common.by import By

serv_obj=Service("C:\Mahesh\chromedriver-win64\chromedriver.exe")
driver=webdriver.Chrome(service=serv_obj)

driver.get("https://opensource-demo.orangehrmlive.com/")
driver.maximize_window()

time.sleep(5)
driver.find_element(By.XPATH,"//a[normalize-space()='OrangeHRM, Inc']").click()
windowIDs =driver.window_handles

print("Window ID of first browser window is :" +windowIDs[0])
print("Window ID of second browser window is :" +windowIDs[1])

time.sleep(3)

'''#Approach-1
parentwindow=windowIDs[0]
childwindow=windowIDs[1]

driver.switch_to.window(parentwindow)
print("Title of parent window:"+driver.title)
time.sleep(3)
driver.switch_to.window(childwindow)
print("Title of child window:"+driver.title)'''

#Approach-2
'''for ID in windowIDs:
    driver.switch_to.window(ID)
    print("Title of Browser Windows are:"+driver.title)'''

#Approach-3-close specific window or multiple windows by using and and or conditions
time.sleep(3)
for ID in windowIDs:
    driver.switch_to.window(ID)
    print(ID)
    if driver.title=="Human Resources Management Software | OrangeHRM" or driver.title=="OrangeHRM":
        driver.close()
