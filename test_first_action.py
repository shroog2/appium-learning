
from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy

options = UiAutomator2Options()
options.platform_name = "Android"
options.device_name = "Android Emulator"
options.app_package = "io.appium.android.apis"
options.app_activity = ".ApiDemos"

driver = webdriver.Remote(
    "http://127.0.0.1:4723",
    options=options
)

try:
    # Check the first element
    accessibility = driver.find_element(
        AppiumBy.ACCESSIBILITY_ID,
        "Accessibility"
    )
    assert accessibility.is_displayed()
    print("Accessibility: PASS")

    # Check the second element
    animation = driver.find_element(
        AppiumBy.ACCESSIBILITY_ID,
        "Animation"
    )
    assert animation.is_displayed()
    print("Animation: PASS")

finally:
    driver.quit()