from time import sleep
from os import path
import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options

path_d = path.join(os.getcwd(), "driver")

path_chrome = path.join(os.getcwd(), "driver/chrome/linux/111.0.5563/chrome")

chromedriver = ChromeDriverManager(path=path_d, version="111.0.5563.110").install()
service = Service(chromedriver)

options = Options()
options.binary_location = path_chrome

driver = webdriver.Chrome(service=service,options=options)

print('foi')
driver.get('https://google.com/')

sleep(10)
driver.close()