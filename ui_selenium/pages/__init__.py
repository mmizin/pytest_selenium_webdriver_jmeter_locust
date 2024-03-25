from dataclasses import dataclass, field
from abc import ABC, abstractmethod
from typing import Union
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver import Chrome, Edge, Firefox
from selenium import webdriver


@dataclass
class Page(ABC):
    url: str
    driver: Union[Chrome, Firefox, Edge] = field(default_factory=Union)
    wait: WebDriverWait = 10
    
    def open(self):
        self.driver.get(self.url)
    