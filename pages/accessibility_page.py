
from appium.webdriver.common.appiumby import AppiumBy


class AccessibilityPage:
    def __init__(self, driver):
        self.driver = driver

    def is_node_provider_displayed(self):
        element = self.driver.find_element(
            AppiumBy.ACCESSIBILITY_ID,
            "Accessibility Node Provider"
        )
        return element.is_displayed()
