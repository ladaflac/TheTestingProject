from page_model.locators import TopNavigationLocators, HeaderLocators, PaymentsLocators, CommonLocators


class BasePage():
    """Class containing the elements present on all pages"""
    def __init__(self, context):
        self.driver = context

    # top sections on each page

    def user_menu(self):
        return self.driver.find_element(*HeaderLocators.USER_MENU)

    def top_nav_offerings(self):
        return self.driver.find_element(*TopNavigationLocators.OFFERINGS_NAV)

    def top_nav_payments(self):
        return self.driver.find_element(*TopNavigationLocators.PAYMENTS_NAV)


    # frame below the menu

    def main_iframe(self):
        return self.driver.find_element(*CommonLocators.MAIN_IFRAME)

    def iframe_title(self):
        return self.driver.find_element(*CommonLocators.IFRAME_TITLE)


    # payments

    def payments_menu(self):
        return self.driver.find_element(*PaymentsLocators.PAYMENTS_MENU)

    def acc_transfer(self):
        return self.driver.find_element(*PaymentsLocators.ACC_TRANSFER)
