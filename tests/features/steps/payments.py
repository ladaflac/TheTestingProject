from behave import then, given, when
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from base_page import BasePage


@given('The Account transfer input page is opened')
def step_impl(context):
    context.execute_steps(u'''
        Given The user is logged in the application
        When The user hovers over 'Payments' in the top menu
        When The user clicks the 'Account transfer' on the Payments menu
    ''')
    WebDriverWait(context.driver, 10).until(expected_conditions.frame_to_be_available_and_switch_to_it(BasePage.main_iframe(context)))
    title = BasePage.iframe_title(context)
    assert title.get_attribute('text') == 'Account transfer - Enter', \
        "Page title is '%s' instead of 'Account transfer - Enter'" % (title.get_attribute('text'))
    context.driver.switch_to.default_content()

@when('The user enters mandatory payment fields')
def step_impl(context):
    pass

@when('The user submits the data')
def step_impl(context):
    pass

@then('The confirmation page is opened')
def step_impl(context):
    pass

@then('The success message is displayed')
def step_impl(context):
    pass

@when('The user does not enter all mandatory payment details')
def step_impl(context):
    pass

@then('The error message is displayed')
def step_impl(context):
    pass
