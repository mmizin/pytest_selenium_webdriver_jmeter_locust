import allure
import pytest
import requests

from _pytest.nodes import Item


from _pytest.config.argparsing import Parser
from config import DriverTypes

pytest_plugins = [
    "ui_selenium.plugins.setup",
    "ui_selenium.plugins.runtest_makereport",
]


def pytest_addoption(parser: Parser) -> None:
    """Reads parameters from pytest command line."""

    parser.addoption(
        "--webdriver",
        action="store",
        choices=DriverTypes.list_items(),
        default="chrome",
        help="driver to run tests against",
    )

    parser.addoption(
        "--url",
        action="store",
        default="http://127.0.0.1:8000/",
        help="driver to run tests against",
    )
