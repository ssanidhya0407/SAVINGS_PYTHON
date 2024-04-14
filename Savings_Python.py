from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from datetime import date
from bs4 import BeautifulSoup as bs
import time
import requests
import random

d1 = date.today().strftime("%d-%m-%Y")

chrome_options=webdriver.ChromeOptions()
chrome_options.add_argument('--disable-notifications')
chrome_options.add_argument("--headless")
url=('https://www.moneycontrol.com/mutual-funds/nav/icici-prudential-equity-debt-fund/MPI011')
driver = webdriver.Chrome("C:/Users/DELL/Downloads/chromedriver", options=chrome_options)
driver.get(url)

element = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, "/html/body/section/div/section[4]/div/div/ul/li[3]/a"))
)
element.click()


driver.find_element("xpath", "//*[@id='onetime_value']").clear()
driver.find_element("xpath", "//*[@id='onetime_value']").send_keys("150000")
driver.find_element("xpath", "//*[@id='onetime_invest_datepicker']").clear()
driver.find_element("xpath", "//*[@id='onetime_invest_datepicker']").send_keys("20-11-2017")
driver.find_element("xpath", "//*[@id='onetime_sell_datepicker']").clear()
driver.find_element("xpath", "//*[@id='onetime_sell_datepicker']").send_keys(d1)
driver.find_element("xpath", "/html/body/section/div/section[4]/div/div/div/div[3]/div[2]/div[1]/div[2]/div[3]/button").click()
WebDriverWait(driver, 2)
curvalue=driver.find_element("xpath", "//*[@id='latestNAVTotal1']").text
print(curvalue)






