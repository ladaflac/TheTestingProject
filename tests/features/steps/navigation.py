from behave import given, when
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators import CommonLocators
from base_page import LoginPage
from page_model.base_page import BasePage
from highlight_elements import HighlightElements


@given("The user is logged in the application")
def step_impl(context):
    # the application page is loaded
    WebDriverWait(context.driver, 10).until(expected_conditions.visibility_of(LoginPage.ebanking_title(context)))
    LoginPage.demo_app_link(context).click()
    # close the welcome message
    WebDriverWait(context.driver, 10).until(expected_conditions.presence_of_element_located(CommonLocators.WELCOME_MSG)).click()
    # check username
    username = BasePage.user_menu(context)
    HighlightElements.highlight(context, username)
    assert username.text == 'DG', "Username is incorrect"


@when("The user opens the 'Payments' menu in the top navigation")
def step_impl(context):
    payments_top_menu = BasePage.top_nav_payments(context)
    HighlightElements.highlight(context, payments_top_menu)
    payments_top_menu.click()
    WebDriverWait(context.driver, 5).until((expected_conditions.visibility_of(BasePage.payments_dropdown(context))))


@when("The user selects the 'Account transfer' on the Payments menu")
def step_impl(context):
    acc_trsf_menu = BasePage.acc_transfer(context)
    HighlightElements.highlight(context, acc_trsf_menu)
    acc_trsf_menu.click()


# @when("The user clicks the 'Offerings' on the top menu")
# def step_impl(context):
#     offerings_top_menu = BasePage.top_nav_offerings(context)
#     HighlightElements.highlight(context, offerings_top_menu)
#     offerings_top_menu.click()
