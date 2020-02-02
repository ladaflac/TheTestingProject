from behave import given, then
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from page_model.accounts_page import AccountFields
from highlight_elements import HighlightElements


@given("The accounts are displayed")
def step_impl(context):
    context.execute_steps(u'''
            Given The user is logged in the application
        ''')
    accounts_table = WebDriverWait(context, 5).until(expected_conditions.visibility_of(AccountFields.account_list(context)))
    HighlightElements.highlight(context, accounts_table)


@given('The account type is "{account_type}"')
def step_impl(context, account_type):
    # find acc types on the screen
    account_types = AccountFields.account_types(context)
    # if acc type equals the account_type from scenario, save its balance type to context
    for acc_type in account_types:
        HighlightElements.highlight(context, acc_type)
        if acc_type.text == account_type:
            # todo account value type should be read from the same row as account type (element doesn't support index!)
            context.acc_value_type = AccountFields.account_value_type(context)
            # HighlightElements.highlight(context, AccountFields.account_value_type(context))
            break
        else:
            continue

@then('Account balance is "{value_type}"')
def step_impl(context, value_type):
    if value_type == 'currency':
        assert context.acc_value_type.text in ('EUR', 'CHF', 'USD'), 'Account balance does not have expected currency'
    # fails because always the first value type is retrieved
    if value_type == 'points':
        assert context.acc_value_type.text == 'ePoints', 'Loyalty account does not have a valid points name'
    else:
        pass
