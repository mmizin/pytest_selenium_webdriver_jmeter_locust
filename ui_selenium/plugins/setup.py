import pytest

from ui_selenium.utilities.webdrivers import get_driver


@pytest.fixture(scope='class')
def setup(request):
    driver_type = request.config.getoption('--webdriver')
    url = request.config.getoption('--url')

    driver = get_driver(driver_type)
    yield driver, url
    driver.quit()
