from page_model.base_page import BasePage
from page_model.locators import HomepageLocators


class AccountFields(BasePage):
    def account_list(self):
        return self.driver.find_element(*HomepageLocators.ACCOUNT_TABLE)

    def account_details(self):
        return self.driver.find_elements(*HomepageLocators.ACCOUNT_ROW)

    def account_types(self):
        return self.driver.find_elements(*HomepageLocators.ACCOUNT_TYPES)

    def account_value_type(self):
        return self.driver.find_element(*HomepageLocators.ACCOUNT_VALUE_TYPE)
