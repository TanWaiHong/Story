from selenium import webdriver
import time

chrome_driver_path = "C:/Users/User/Desktop/coding/store/chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver_path)
driver.get("http://orteil.dashnet.org/experiments/cookie/")

items = driver.find_elements_by_css_selector("#store div")
item_ids = [item.get_attribute("id") for item in items]

cookie = driver.find_element_by_id("cookie")

timeout = time.time() + 5
five_min = time.time() + 60 * 5

while time.time() < five_min:
    if time.time() > timeout:

        all_prices = driver.find_elements_by_css_selector("#store b")
        item_prices = [int(price.text.split("-")[1].strip().replace(",", "")) for price in all_prices if price.text != ""]

        cookie_upgrades = dict()
        for n in range(len(item_prices)):
            cookie_upgrades[item_prices[n]] = item_ids[n]

        money_element = driver.find_element_by_id("money").text
        if "," in money_element:
            money_element = money_element.replace(",", "")
        cookie_count = int(money_element)

        affordable_upgrades = {}
        for cost, the_id in cookie_upgrades.items():
            if cookie_count > cost:
                affordable_upgrades[cost] = the_id

        if affordable_upgrades:
            highest_price_affordable_upgrade = max(affordable_upgrades)
            to_purchase_id = affordable_upgrades[highest_price_affordable_upgrade]

            driver.find_element_by_id(to_purchase_id).click()

        timeout += 5

    cookie.click()

the_time = time.time() + 60 * 30
while time.time() < the_time:
    time.sleep(10)
    all_prices = driver.find_elements_by_css_selector("#store b")
    item_prices = [int(price.text.split("-")[1].strip().replace(",", "")) for price in all_prices if price.text != ""]

    cookie_upgrades = dict()
    for n in range(len(item_prices)):
        cookie_upgrades[item_prices[n]] = item_ids[n]

    money_element = driver.find_element_by_id("money").text
    if "," in money_element:
        money_element = money_element.replace(",", "")
    cookie_count = int(money_element)

    affordable_upgrades = {}
    for cost, the_id in cookie_upgrades.items():
        if cookie_count > cost:
            affordable_upgrades[cost] = the_id

    if affordable_upgrades:
        highest_price_affordable_upgrade = max(affordable_upgrades)
        to_purchase_id = affordable_upgrades[highest_price_affordable_upgrade]

        driver.find_element_by_id(to_purchase_id).click()


