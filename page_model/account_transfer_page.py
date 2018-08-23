from page_model.base_page import BasePage
from page_model.locators import PaymentsLocators


class AccountTransferPage(BasePage):
    def payment_form_input(self):
        return self.driver.find_element(*PaymentsLocators.PAYMENT_FORM_INPUT)

    def payment_form_confirm(self):
        return self.driver.find_element(*PaymentsLocators.PAYMENT_FORM_CHECK)


class AccountTransferPageFields(BasePage):
    def credit_acc_list(self):
        return self.driver.find_element(*PaymentsLocators.CREDIT_ACC_LIST)

    def credit_acc(self):
        return self.driver.find_element(*PaymentsLocators.CREDIT_ACC)

    def amount(self):
        return self.driver.find_element(*PaymentsLocators.AMOUNT)

    def reason_for_payment(self):
        return self.driver.find_element(*PaymentsLocators.REASON_FOR_PAYMENT)

    def execution_date(self):
        return self.driver.find_element(*PaymentsLocators.EXEC_DATE)

    def submit(self):
        return self.driver.find_element(*PaymentsLocators.SUBMIT_BUTTON)

    def error_container(self):
        return self.driver.find_element(*PaymentsLocators.ERROR_CONTAINER)

    def error_message(self):
        return self.driver.find_element(*PaymentsLocators.ERROR_MESSAGE)

    def payment_status(self):
        return self.driver.find_element(*PaymentsLocators.PAYMENT_STATUS)
