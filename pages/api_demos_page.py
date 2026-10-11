
from appium.webdriver.common.appiumby import AppiumBy


class ApiDemosPage:
    def __init__(self, driver):
        self.driver = driver

    def open_accessibility(self):
        self.driver.find_element(
            AppiumBy.ACCESSIBILITY_ID,
            "Accessibility"
        ).click()
