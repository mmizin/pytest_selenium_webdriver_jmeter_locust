import pytest

from ui_selenium.utilities.webdrivers import get_driver
from selenium import webdriver


@pytest.fixture(scope='class')
def setup(request) -> tuple[webdriver, str]:
    driver_type = request.config.getoption('--webdriver')
    # url = request.config.getoption('--url')
    driver = get_driver(driver_type)

    yield driver
    driver.close()
    driver.quit()
