from page_model.locators import TopNavigationLocators, HeaderLocators, PaymentsLocators


class BasePage():
    """Class containing the elements present on all pages"""
    def __init__(self, context):
        self.driver = context

    def user_menu(self):
        return self.driver.find_element(*HeaderLocators.USER_MENU)

    def top_nav_offerings(self):
        return self.driver.find_element(*TopNavigationLocators.OFFERINGS_NAV)

    def top_nav_payments(self):
        return self.driver.find_element(*TopNavigationLocators.PAYMENTS_NAV)

    def payments_menu(self):
        return self.driver.find_element(*PaymentsLocators.PAYMENTS_MENU)

    def acc_transfer(self):
        return self.driver.find_element(*PaymentsLocators.ACC_TRANSFER)
