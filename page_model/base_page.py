from page_model.locators import TopNavigationLocators, HeaderLocators, PaymentsLocators, CommonLocators


class BasePage:
    """Class containing the elements present on all pages"""
    def __init__(self, context):
        self.driver = context

    # top sections on each page

    def user_menu(self):
        return self.driver.find_element(*HeaderLocators.USER_MENU)

    # def top_nav_offerings(self):
    #     return self.driver.find_element(*TopNavigationLocators.OFFERINGS_NAV)

    def top_nav_payments(self):
        return self.driver.find_element(*TopNavigationLocators.PAYMENTS_NAV)

    def payments_dropdown(self):
        return self.driver.find_element(*PaymentsLocators.PAYMENTS_MENU_OPTIONS)

    def acc_transfer(self):
        return self.driver.find_element(*PaymentsLocators.ACC_TRANSFER)


class LoginPage(BasePage):
    """Class containing the elements related to login"""

    def demo_app_link(self):
        return self.driver.find_element(*CommonLocators.DEMO_APP_LINK)

    def ebanking_title(self):
        return self.driver.find_element(*CommonLocators.EBANKING_PAGE_TITLE)