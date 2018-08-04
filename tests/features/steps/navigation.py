from behave import given, when
from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from page_model.base_page import BasePage


@given("The user is logged in the application")
def step_impl(context):
    username = BasePage.user_menu(context).text
    assert username == 'UBS Demo', "Username is incorrect"


@when("The user clicks the 'Offerings' on the top menu")
def step_impl(context):
    BasePage.top_nav_offerings(context).click()


@when("The user hovers over 'Payments' in the top menu")
def step_impl(context):
    ActionChains(context.driver).move_to_element(BasePage.top_nav_payments(context)).perform()
    WebDriverWait(context.driver, 10).until(expected_conditions.visibility_of(BasePage.payments_menu(context)))


@when("The user clicks the 'Account transfer' on the Payments menu")
def step_impl(context):
    BasePage.acc_transfer(context).click()
