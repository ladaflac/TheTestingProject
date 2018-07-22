from page_model.locators import TopNavigationLocators, HeaderLocators


class BasePage():
    """Class containing the elements present on all pages"""
    def __init__(self, context):
        self.driver = context

    def user_menu(self):
        return self.driver.find_element(*HeaderLocators.USER_MENU)

    def top_nav_offerings(self):
        return self.driver.find_element(*TopNavigationLocators.OFFERINGS_NAV)

