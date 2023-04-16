import os.path
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

class ChromeDriver:
    def __init__(self, driver_path):
        self.driver_path = driver_path
        self.prefs = {
            "download.default_directory" : "/home/nathan/projects/ankicards-automation/files"
        }

    def setup(self):
        chrome_options = webdriver.ChromeOptions()
        # chrome_options.add_argument("--headless")
        # chrome_options.add_argument("--no-sandbox")       
        chrome_options.add_experimental_option("prefs", self.prefs)
        homedir = os.path.expanduser("~")
        webdriver_service = Service(f"{homedir}/chromedriver/stable/chromedriver")
        return webdriver.Chrome(service=webdriver_service, options=chrome_options)
