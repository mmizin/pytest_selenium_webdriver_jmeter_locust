from ui_selenium.pages.home_page import HomePage


class TestHomePage:
    def test_open_home_page(self, setup):
        page = HomePage(driver=setup)

        page.open()
    

    
