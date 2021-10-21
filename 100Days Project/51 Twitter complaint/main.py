from selenium import webdriver
from ISTB import InternetSpeedTwitterBot

PROMISED_DOWN = 150
PROMISED_UP = 30
CHROME_DRIVER_PATH = "C:/Users/User/Desktop/coding/store/chromedriver.exe"
TWITTER_EMAIL = "hongworkonly@gmail.com"
TWITTER_PASSWORD = "KkmSD2p5BNkhCxn"
TWITTER_USER_NAME = "TanWaiHong6"

bot = InternetSpeedTwitterBot(CHROME_DRIVER_PATH)
bot.get_internet_speed()

bot.tweet_at_provider(TWITTER_EMAIL, TWITTER_USER_NAME, TWITTER_PASSWORD)

bot.driver.close()
