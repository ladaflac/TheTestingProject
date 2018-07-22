from behave import given, when
from page_model.base_page import BasePage


@given("The user is logged in the application")
def step_impl(context):
    username = BasePage.user_menu(context).text
    assert username == 'UBS Demo', "Username is incorrect"

@when("The user clicks the 'Offerings' on the top menu")
def step_impl(context):
    BasePage.top_nav_offerings(context).click()
