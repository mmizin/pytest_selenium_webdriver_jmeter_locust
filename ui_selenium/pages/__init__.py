from dataclasses import dataclass, field
from abc import ABC, abstractmethod
from typing import Union, Tuple
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver import Chrome, Edge, Firefox
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


@dataclass
class Page(ABC):
    url: str
    driver: Union[Chrome, Firefox, Edge] = field(default_factory=Union)
    wait: WebDriverWait = 10
    
    def open(self) -> None:
        self.driver.get(self.url)
    
    def presence_of_element_located(self, locator_with_selector: Tuple[By, str], wait: int = wait) -> WebElement:
        return WebDriverWait(self.driver, wait).until(EC.presence_of_element_located(locator_with_selector))
        
