
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

ops=webdriver.ChromeOptions()
ops.add_argument("--disable-notifications")

serv_obj=Service("C:/Mahesh/chromedriver-win64/chromedriver.exe")
driver=webdriver.Chrome(service=serv_obj,options=ops)


driver.get("http://wheremylocation.com/")
driver.maximize_window()