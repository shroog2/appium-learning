from appium import webdriver
from appium.options.android import UiAutomator2Options

options = UiAutomator2Options()
options.platform_name = "Android"
options.device_name = "emulator-5554"
options.app_package = "io.appium.android.apis"
options.app_activity = ".ApiDemos"
driver = webdriver.Remote(
    "http://127.0.0.1:4723",
    options=options
)
print("Connected successfully!")
print(driver.current_package)
print(driver.capabilities)
driver.save_screenshot("screen.png")
driver.press_keycode(3)