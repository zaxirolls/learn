from selenium import webdriver
import chromedriver_binary
import time

driver = webdriver.Chrome()
driver.get('https://www.google.com/')
time.sleep(10)
driver.quit()