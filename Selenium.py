from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
time.sleep(5)
driver.get('https://coinmarketcap.com/')
time.sleep(5)