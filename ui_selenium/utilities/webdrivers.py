from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from .. config import DriverTypes


def get_driver(driver_type):
    if driver_type == DriverTypes.CHROME.browser:
        return webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    elif driver_type == DriverTypes.FIREFOX.browser:
        return webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
