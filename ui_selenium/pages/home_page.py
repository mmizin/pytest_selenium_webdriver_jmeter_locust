from typing import Union
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver import Chrome, Edge, Firefox
from ui_selenium.pages import Page


class HomePage(Page):
    url = "http://127.0.0.1:8000/"
    
    def __init__(self, driver: Union[Chrome, Firefox, Edge], url: str = None, wait: WebDriverWait = 10) -> None:
        super().__init__(url or HomePage.url, driver, wait)
    
        
    