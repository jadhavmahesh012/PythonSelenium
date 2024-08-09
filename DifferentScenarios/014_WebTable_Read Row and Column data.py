import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

serv_obj=Service("C:/Mahesh/chromedriver-win64/chromedriver.exe")
driver=webdriver.Chrome(service=serv_obj)

driver.get("https://cosmocode.io/automation-practice-webtable/")
time.sleep(2)
driver.maximize_window()

#1.Read specific row and column data
country_name=driver.find_element(By.XPATH,"//div[@class='entry-content']//tbody//tr[2]//td[2]").text
print("1.First country name is:"+country_name)


#2.Read data based on condition 


driver.close()