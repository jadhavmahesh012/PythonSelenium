import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


serv_obj=Service("C:/Mahesh/chromedriver-win64/chromedriver.exe")
driver=webdriver.Chrome(service=serv_obj)


driver.get("https://admin-demo.nopcommerce.com/")
driver.maximize_window()

time.sleep(2)


driver.find_element(By.XPATH,"//input[@id='Email']").clear()
time.sleep(2)
driver.find_element(By.XPATH,"//input[@id='Email']").send_keys("admin@yourstore.com")
time.sleep(2)

driver.find_element(By.XPATH,"//input[@id='Password']").clear()
time.sleep(2)
driver.find_element(By.XPATH,"//input[@id='Password']").send_keys("admin")
time.sleep(2)

driver.find_element(By.XPATH,"//button[@type='submit']").click()

act_title=driver.title

if act_title=="Dashboard / nopCommerce administration":
    print("login test passed")

else:
    driver.save_screenshot("../Screenshots/DifferentCommands.png")
    print("login test failed")

#Wait command-time.sleep(--time in Second--)
time.sleep(2)

#Application commands-get(),title,current_url,page_source
Title=driver.title
URL=driver.current_url
pagesrc=driver.page_source

print("current URL is:",URL)
print("current title is:",Title)
print("Pagesource is:",pagesrc)
time.sleep(2)

#Navigational commands-back(),forward(),refresh()
driver.refresh()
time.sleep(2)

driver.back()
time.sleep(2)

#browser commands-close() ,quit()
driver.close()
