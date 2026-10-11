
from pages.api_demos_page import ApiDemosPage
from pages.accessibility_page import AccessibilityPage


def test_navigate_to_accessibility(driver):
    home_page = ApiDemosPage(driver)
    accessibility_page = AccessibilityPage(driver)

    home_page.open_accessibility()

    assert accessibility_page.is_node_provider_displayed()
