
import pytest
from appium import webdriver
from appium.options.android import UiAutomator2Options


@pytest.fixture
def driver():
    options = UiAutomator2Options()
    options.platform_name = "Android"
    options.device_name = "Android Emulator"
    options.app_package = "io.appium.android.apis"
    options.app_activity = ".ApiDemos"

    app_driver = webdriver.Remote(
        "http://127.0.0.1:4723",
        options=options
    )

    yield app_driver

    app_driver.quit()