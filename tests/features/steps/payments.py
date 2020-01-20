from time import sleep
from behave import then, given, when, step
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from highlight_elements import HighlightElements
from page_model.account_transfer_page import AccountTransferPageFields, AccountTransferPage
from db import DataParser, SaveDataToDb, GetDataFromDb


@given('The Account transfer input page is opened')
def step_impl(context):
    context.execute_steps(u'''
        Given The user is logged in the application
        When The user opens the 'Payments' menu in the top navigation
        When The user selects the 'Account transfer' on the Payments menu
    ''')
    sleep(2)
    WebDriverWait(context.driver, 10).until(expected_conditions.visibility_of(AccountTransferPage.payment_form_input(context)))


@when('The user enters mandatory payment fields')
def step_impl(context):

    AccountTransferPageFields.debit_acc_list(context).click()
    AccountTransferPageFields.debit_acc(context).click()
    sleep(1)
    AccountTransferPageFields.credit_acc_list(context).click()
    AccountTransferPageFields.credit_acc(context).click()

    # upit u bazu samo jednom za sva polja
    amount_reason_date_dict = DataParser.input_data_fields(context)

    amount = amount_reason_date_dict['AMOUNT']
    AccountTransferPageFields.amount(context).click()
    AccountTransferPageFields.amount(context).send_keys(str(amount))

    # skipping the reason for payment field, it is not mandatory anymore
    # reason_for_payment = amount_reason_date_dict['REASON_FOR_PAYMENT']
    # AccountTransferPageFields.reason_for_payment(context).send_keys(reason_for_payment)

    # todo adjust the input of date to the new date format
    # yyyy, mm, dd = amount_reason_date_dict['EXECUTION_DATE'].split('-')
    # execution_date = dd + '.' + mm + '.' + yyyy
    # AccountTransferPageFields.execution_date(context).click()
    # AccountTransferPageFields.execution_date(context).clear()
    # AccountTransferPageFields.execution_date(context).send_keys(execution_date)

    # save input data dict to context in order to use it in the next steps
    context.new_payment_data = amount_reason_date_dict


@step('The user submits the form')
def step_impl(context):
    HighlightElements.highlight(context, AccountTransferPageFields.submit(context))
    AccountTransferPageFields.submit(context).click()


@then('The success message is displayed')
def step_impl(context):
    WebDriverWait(context.driver, 10).until(expected_conditions.url_contains("payment-wizard"))
    sleep(1)
    order_status = AccountTransferPageFields.payment_status(context).text
    assert order_status.startswith('Your order has been accepted') == True, "Actual status is '%s'" % order_status

    # check the previous number of orders in the database - only if payment was successful
    orders_count_before = len(GetDataFromDb.get_all_payments(context))
    context.orders_count_before = orders_count_before


@then('Payment is saved')
def step_impl(context):
    # I don't have access to this application's real db, so I am saving a payment copy to Airtable db
    payment_data_to_save = context.new_payment_data
    SaveDataToDb.create_new_payment(context, payment_data_to_save)
    # todo: assert response status


@then('The number of transfers in the database increases by 1')
def step_impl(context):
    orders_count_after = len(GetDataFromDb.get_all_payments(context))
    orders_increase = orders_count_after - context.orders_count_before
    assert orders_increase == 1, "Orders count increased by %d instead by 1" % orders_increase


# todo fix this: find a way to read the error msg
# @then('The error message is displayed')
# def step_impl(context):
#     sleep(2)
#     error_message = AccountTransferPageFields.error_message(context).get_attribute('textContent')
#     assert error_message == 'Please fill out this field', "Actual message is '%s'" % error_message
