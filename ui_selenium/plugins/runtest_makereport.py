import pytest

from ui_selenium.utilities.screenshot import allure_full_page_screenshot


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    if rep.when == 'call' and rep.failed:
        allure_full_page_screenshot(driver=item.cls.driver, name=item.nodeid)