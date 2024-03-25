from enum import Enum
from enum import unique
from types import DynamicClassAttribute
from typing import List


@unique
class DriverTypes(Enum):
    CHROME = "chrome"
    FIREFOX = "firefox"
    
    @DynamicClassAttribute
    def browser(self) -> str:
        return {
            self.CHROME: self.CHROME.value,
            self.FIREFOX: self.FIREFOX.value,
        }[self]
    
    @classmethod
    def list_items(cls) -> List[str]:
        return [cls.CHROME.browser, cls.FIREFOX.browser]
    
    

