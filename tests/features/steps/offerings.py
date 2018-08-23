from behave import given, then
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from page_model.base_page import BasePage
from page_model.locators import OfferingsLocators


@given("The Offerings page is opened")
def step_impl(context):
    context.execute_steps(u'''
        Given The user is logged in the application
        When The user clicks the 'Offerings' on the top menu
    ''')
    WebDriverWait(context.driver, 10).until(expected_conditions.frame_to_be_available_and_switch_to_it(BasePage.main_iframe(context)))
    title = BasePage.iframe_title(context)
    assert title.get_attribute('text') == 'Sales and Offering Space', \
        "Page title is '%s' instead of 'Sales and Offering Space'" % (title.get_attribute('text'))
    context.driver.switch_to.default_content()

@then("The user sees the menu with all products")
def step_impl(context):
    context.driver.switch_to_frame('bzeMainIframe')
    offerings_overview = WebDriverWait(context.driver, 10).until(expected_conditions.element_to_be_clickable(OfferingsLocators.OVERVIEW))
    assert offerings_overview.text.startswith('Overview'), "The Overview section is not present"
    context.driver.switch_to.default_content()
