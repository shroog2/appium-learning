
from appium.webdriver.common.appiumby import AppiumBy


def test_animation(driver):
    element = driver.find_element(
        AppiumBy.ACCESSIBILITY_ID,
        "Animation"
    )

    assert element.is_displayed()