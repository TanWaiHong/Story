import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import os
import wget

keyword = input("keyword\n")
jpg_count = int(input("jpg count\n"))


PATH = "C:/Users/User/Desktop/coding/chromedriver.exe"
driver = webdriver.Chrome(PATH)
driver.get("https://www.instagram.com/")

username = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.NAME, "username"))
)

password = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.NAME, "password"))
)
login = driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[3]/button')

username.clear()
password.clear()
username.send_keys('hongttisme')
password.send_keys('75031010a')
login.click()

search = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, '//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/input'))
)

search.send_keys(keyword)

time.sleep(1)
search.send_keys(Keys.RETURN)

time.sleep(1)
search.send_keys(Keys.RETURN)

WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.CLASS_NAME, 'FFVAD'))
)

for i in range(jpg_count):
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")  # java指令
    time.sleep(5)

imgs = driver.find_elements_by_class_name('FFVAD')

download_path = os.path.join(keyword)
os.mkdir(download_path)

count = 0
for img in imgs:
    save_as = os.path.join(download_path, keyword + str(count) + '.jpg')
    wget.download(img.get_attribute("src"), save_as)
    count += 1

driver.quit()
