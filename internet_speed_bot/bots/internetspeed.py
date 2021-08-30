from selenium import webdriver
import time
import logging
from config import create_api

CHROME_DRIVER_PATH = "C:\Development\chromedriver.exe"

logging.basicConfig(filename="speedtest.log",
                    level=logging.INFO,
                    format='%(asctime)s:%(levelname)s:%(message)s',
                    datefmt='%m/%d/%Y %I:%M:%S %p',)
logger = logging.getLogger()


class InternetSpeedBot:

    def __init__(self):
        self.driver = webdriver.Chrome(CHROME_DRIVER_PATH)

    def get_internet_speed(self):

        # go to speedtest.com to check current internet speed
        self.driver.maximize_window()
        self.driver.get(url="https://www.speedtest.net/result/11176815248")
        time.sleep(5)
        go_button = self.driver.find_element_by_xpath(
            '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[1]/a/span[4]')
        go_button.click()

        # after test is complete get the up and download speeds
        time.sleep(90)
        self.down = self.driver.find_element_by_xpath(
            '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]'
            '/div/div/div[2]/div[1]/div[2]/div/div[2]/span').text
        self.up = self.driver.find_element_by_xpath(
            '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]'
            '/div/div/div[2]/div[1]/div[3]/div/div[2]/span').text

        # log speed test in file
        logger.info(f"Download speed: {self.down} || Upload speed: {self.up}")
        self.driver.quit()

        return self.down, self.up

    def tweet_at_provider(self, provider):
        # logger.info("Tweeting at provider: ")
        api = create_api()
        internet_provider = api.get_user(provider)
        api.update_status(
            status=f"Hey @{internet_provider.screen_name}"
                   f" why is my internet speed {self.down}download & {self.up}upload when I pay for 200down/10up?"
        )
