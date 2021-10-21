from selenium import webdriver
import time
from selenium.common.exceptions import NoSuchElementException


class InternetSpeedTwitterBot:
    def __init__(self, driver_path):
        self.driver = webdriver.Chrome(executable_path=driver_path)
        self.up = 0
        self.down = 0

    def get_internet_speed(self):
        self.driver.get("https://www.speedtest.net/")
        time.sleep(3)
        start_button = self.driver.find_element_by_css_selector(".start-text")
        start_button.click()
        time.sleep(60)
        self.up = self.driver.find_element_by_css_selector(".upload-speed").text
        self.down = self.driver.find_element_by_css_selector(".download-speed").text

    def tweet_at_provider(self, mail, user, key):
        self.driver.get("https://twitter.com/home")
        time.sleep(6)

        email_input = self.driver.find_element_by_xpath(
            '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div[2]/label/div/div[2]/div/input')
        email_input.send_keys(mail)
        next_button = self.driver.find_element_by_xpath(
            '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div')
        next_button.click()

        try:
            time.sleep(2)
            name_input = self.driver.find_element_by_xpath(
                '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div[2]/label/div/div[2]/div/input')
            name_input.send_keys(user)
            next_button = self.driver.find_element_by_xpath(
                '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div')
            next_button.click()

        except NoSuchElementException:
            pass

        time.sleep(2)
        key_input = self.driver.find_element_by_xpath(
            '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div[2]/div/label/div/div[2]/div/input')
        key_input.send_keys(key)
        log_in_button = self.driver.find_element_by_xpath(
            '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div')
        log_in_button.click()

        time.sleep(3)
        post_input = self.driver.find_element_by_xpath(
            '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[1]/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/label/div[1]/div/div/div/div/div[2]/div/div/div/div')
        post_input.send_keys(f"up: {self.up}, down: {self.down}")
        post_button = self.driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[1]/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[3]/div/div/div[2]/div[3]/div')
        post_button.click()
