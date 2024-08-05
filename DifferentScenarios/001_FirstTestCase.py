from selenium import webdriver
from selenium.webdriver.chrome import options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

serv_obj=Service("C:/Mahesh/chromedriver-win64/chromedriver.exe")
driver=webdriver.Chrome(service=serv_obj)

#driver=webdriver.Chrome()

driver.get("https://admin-demo.nopcommerce.com/")


driver.find_element(By.XPATH,"//input[@id='Email']").clear()
driver.find_element(By.XPATH,"//input[@id='Email']").send_keys("admin@yourstore.com")

driver.find_element(By.XPATH,"//input[@id='Password']").clear()
driver.find_element(By.XPATH,"//input[@id='Password']").send_keys("admin")
driver.find_element(By.XPATH,"//button[@type='submit']").click()


act_title=driver.title

if act_title=="Dashboard / nopCommerce administration1":
    print("login test passed")

else:
    driver.save_screenshot("../Screenshots/FirstTestCase.png")
    print("login test failed")
    driver.close()



