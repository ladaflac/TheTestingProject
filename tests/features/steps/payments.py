from behave import then, given, when, step
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from page_model.account_transfer_page import AccountTransferPageFields, AccountTransferPage
from page_model.base_page import BasePage
from db import DataParser, SaveDataToDb


@given('The Account transfer input page is opened')
def step_impl(context):
    context.execute_steps(u'''
        Given The user is logged in the application
        When The user hovers over 'Payments' in the top menu
        When The user clicks the 'Account transfer' on the Payments menu
    ''')
    WebDriverWait(context.driver, 10).until(expected_conditions.frame_to_be_available_and_switch_to_it(BasePage.main_iframe(context)))
    AccountTransferPage.payment_form_input(context)
    context.driver.switch_to.default_content()


@when('The user enters mandatory payment fields')
def step_impl(context):
    context.driver.switch_to_frame(BasePage.main_iframe(context))

    AccountTransferPageFields.credit_acc_list(context).click()
    AccountTransferPageFields.credit_acc(context).click()

    # upit u bazu samo jednom za sva polja
    global amount_reason_date_dict
    amount_reason_date_dict = DataParser.input_data_fields(context)

    amount = amount_reason_date_dict['AMOUNT']
    AccountTransferPageFields.amount(context).send_keys(str(amount))

    reason_for_payment = amount_reason_date_dict['REASON_FOR_PAYMENT']
    AccountTransferPageFields.reason_for_payment(context).send_keys(reason_for_payment)

    yyyy, mm, dd = amount_reason_date_dict['EXECUTION_DATE'].split('-')
    execution_date = dd + '.' + mm + '.' + yyyy
    AccountTransferPageFields.execution_date(context).clear()
    AccountTransferPageFields.execution_date(context).send_keys(execution_date)

    # save input data dict to context in order to use it in the next steps
    context.new_payment_data = amount_reason_date_dict

    context.driver.switch_to.default_content()


@step('The user submits the form')
def step_impl(context):
    context.driver.switch_to_frame(BasePage.main_iframe(context))
    AccountTransferPageFields.submit(context).click()
    context.driver.switch_to.default_content()


@then('The confirmation page is opened')
def step_impl(context):
    WebDriverWait(context.driver, 10).until(expected_conditions.frame_to_be_available_and_switch_to_it(BasePage.main_iframe(context)))
    AccountTransferPage.payment_form_confirm(context)
    context.driver.switch_to.default_content()


@then('The success message is displayed')
def step_impl(context):
    WebDriverWait(context.driver, 10).until(expected_conditions.frame_to_be_available_and_switch_to_it(BasePage.main_iframe(context)))
    order_status = AccountTransferPageFields.payment_status(context).get_attribute('textContent')
    assert order_status == 'Fully approved', "Actual status is '%s'" % order_status

    # save input data to the database only if payment was successful
    payment_data_to_save = context.new_payment_data
    SaveDataToDb.create_new_payment(context, payment_data_to_save)

    context.driver.switch_to.default_content()


@then('The error message is displayed')
def step_impl(context):
    context.driver.switch_to_frame(BasePage.main_iframe(context))
    WebDriverWait(context.driver, 10).until(expected_conditions.visibility_of(AccountTransferPageFields.error_container(context)))
    error_message = AccountTransferPageFields.error_message(context).get_attribute('textContent')
    assert error_message == 'The entries are incomplete or incorrect:', "Actual message is '%s'" % error_message
    context.driver.switch_to.default_content()
