from base_page import BasePage
from locators import PaymentsLocators


class AccountTransferPage(BasePage):
    def submit(self):
        return self.driver.find_element(*PaymentsLocators.SUBMIT_BUTTON)

    def error_container(self):
        return self.driver.find_element(*PaymentsLocators.ERROR_CONTAINER)

    def error_message(self):
        return self.driver.find_element(*PaymentsLocators.ERROR_MESSAGE)
