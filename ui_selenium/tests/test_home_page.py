import allure
import pytest

from ui_selenium.pages.home_page import HomePage
from selenium.webdriver.common.by import By


@allure.epic("TEST epic")
@allure.feature("TEST features")
@allure.story("TEST Authentication")
@allure.title("TEST title")
@pytest.mark.usefixtures('setup')
class TestHomePage:
    
    def test_open_home_page(self):
        page = HomePage(driver=self.driver)

        page.open()
        assert page.presence_of_element_located(locator_with_selector=(By.CLASS_NAME, 'navbar-brand'))
    
    def test_screenshot(self):
        page = HomePage(driver=self.driver)
        
        page.open()
        assert False
