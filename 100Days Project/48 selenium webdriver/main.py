from selenium import webdriver

chrome_driver_path = "C:/Users/User/Desktop/coding/store/chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

# driver.get("https://www.amazon.com/dp/B086FVNKYX?pf_rd_r=RRNXWDVM5G5C97JSKCKB&pf_rd_p=cc71d24e-d8fe-43fc-95a9-568c4f3ddd6a&pd_rd_r=fcfb782a-439b-4e13-803c-3b4a352c2e37&pd_rd_w=C8lnw&pd_rd_wg=wABn9&ref_=pd_gw_unk")
# price = driver.find_element_by_id("priceblock_ourprice")
# print(price.text)

driver.get("https://www.python.org/")
event_time_list = driver.find_elements_by_css_selector(".event-widget time")
event_name_list = driver.find_elements_by_css_selector(".event-widget li a")


event_dict = {x: {"time": event_time_list[x].text, "name": event_name_list[x].text} for x in range(len(event_time_list))}
print(event_dict)
driver.quit()
