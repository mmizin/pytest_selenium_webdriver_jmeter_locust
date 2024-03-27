import allure


def allure_full_page_screenshot(driver, name):
    png_bytes = driver.get_screenshot_as_png()
    allure.attach(
        png_bytes,
        name=name,
        attachment_type=allure.attachment_type.PNG
    )
