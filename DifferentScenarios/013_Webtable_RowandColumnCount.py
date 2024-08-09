import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

serv_obj=Service("C:/Mahesh/chromedriver-win64/chromedriver.exe")
driver=webdriver.Chrome(service=serv_obj)

driver.get("https://www.programiz.com/sql/online-compiler/")
time.sleep(2)
driver.maximize_window()


Rows=len(driver.find_elements(By.XPATH,"//div[@class='output-table']//tr"))
print(Rows)


Columns=len(driver.find_elements(By.XPATH,"//div[@class='output-table']//tr[1]//th"))
print(Columns)
driver.save_screenshot("../Screenshots/webtable_RowsandColumns.png")

time.sleep(3)
driver.close()