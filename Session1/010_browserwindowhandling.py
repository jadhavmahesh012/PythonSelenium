import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common import by
from selenium.webdriver.common.by import By

serv_obj=Service("C:\Mahesh\chromedriver-win64\chromedriver.exe")
driver=webdriver.Chrome(service=serv_obj)
