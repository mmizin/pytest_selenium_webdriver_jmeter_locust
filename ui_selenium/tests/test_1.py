import pytest


class Test1Class(object):
    def test_1(self, setup):
        webdriver, url = setup
        webdriver.get("https://pytest-with-eric.com/pytest-advanced/pytest-addoption/")

    def test_2(self, setup):
        webdriver, url = setup
        webdriver.get("https://www.linkedin.com/feed/")
