from selenium import webdriver
from selenium.webdriver.chrome import options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver=webdriver.Chrome("C:\Mahesh\chromedriver-win64\chromedriver.exe")
driver.get('https://www.globalsqa.com/demo-site/select-dropdown-menu/')
driver.maximize_window()

drp_country=Select(driver.find_element(By.XPATH,"//div[@class='single_tab_div']//p//select"))
#drp_country.select_by_visible_text("India")
drp_country.select_by_value("IND")

#drp_country.select_by_index("20")

alloptions=drp_country.options
print("total number  of options:",len(alloptions))


for option in alloptions:
    #print("All options are:",option.text)

    if option.text=="India":
        print("Found in dropdown")
        break




