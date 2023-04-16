import os
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.by import By
from time import sleep
from dotenv import load_dotenv

load_dotenv()

class Machine:
    def __init__(self, driver: WebDriver, word_list) -> None:
        self.driver = driver
        self.word_list = word_list
        self.login = os.getenv("LOGIN")
        self.password = os.getenv("PASSWORD")

    def download(self, url):
        self.__do_login()

        for word_dict in self.word_list:
            for word in word_dict:
                try:
                    suffix = f"{word}/#ja"
                    self.driver.get(url + suffix)
                    button = self.driver.find_element(By.XPATH, "//p[@class='download']//span[@data-p3='ja']")
                    button.click()
                    sleep(5)
                except:
                    print("Error trying to download file from URL: " + url)

    def __do_login(self):
        self.driver.get("https://forvo.com/login/")
        login_input = self.driver.find_element(By.XPATH, "//input[@name='login']")
        login_input.send_keys(self.login)
        sleep(1)
        password_input = self.driver.find_element(By.XPATH, "//input[@name='password']")
        password_input.send_keys(self.password)
        sleep(1)
        login_button = self.driver.find_element(By.XPATH, "//button[@type='submit']//text()[normalize-space(.)='Enter']/parent::*")
        login_button.click()
        