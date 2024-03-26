from ui_selenium.pages.home_page import HomePage
from selenium.webdriver.common.by import By



class TestHomePage:
    def test_open_home_page(self, setup):
        page = HomePage(driver=setup)

        page.open()
        assert page.presence_of_element_located(locator_with_selector=(By.CLASS_NAME, 'navbar-brand'))
    
