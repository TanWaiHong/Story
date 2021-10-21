from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time

PATH = "C:/Users/User/Desktop/coding/chromedriver.exe"  # 记录chromedriver地址
driver = webdriver.Chrome(PATH)  # 执行chromedriver

driver.get("https://youtube.com")  # 使chromedriver进入指定网站
search = driver.find_element_by_id("search")  # 用id找到搜索栏
# search.clear()    #清空搜索栏，不知道为什么我用不到
search.send_keys("比特币")  # 输入关键字
search.send_keys(Keys.ENTER)  # 输入换行指令

WebDriverWait(driver, 5).until(  # 在driver内，等5秒，直到在driver看到"all" ID 为止
    EC.presence_of_element_located((By.ID, "all"))
)

titles = driver.find_elements_by_id("video-title")  # 搜索视频标题
for title in titles:
    print(title.text)

link = driver.find_element_by_link_text("【震撼】比特幣，人類進入虛擬世界的第一步 | 老高與小茉 Mr & Mrs Gao")
link.click()

time.sleep(1)

driver.back()

driver.forward()

time.sleep(5)
driver.quit()
