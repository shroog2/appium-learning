
from appium.webdriver.common.appiumby import AppiumBy


def test_accessibility(driver):
    element = driver.find_element(
        AppiumBy.ACCESSIBILITY_ID,
        "Accessibility"
    )

    assert element.is_displayed()