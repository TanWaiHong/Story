from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time

PATH = "C:/Users/User/Desktop/coding/chromedriver.exe"
driver = webdriver.Chrome(PATH)

driver.get("https://www.arealme.com/click-speed-test/en/")
start = driver.find_element_by_id("start")

time.sleep(3)
start.click()

click_area = driver.find_element_by_xpath('//*[@id="clickarena"]')
time.sleep(3)

for x in range():
    click_area.click()
