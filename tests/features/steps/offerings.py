from behave import given, then
# from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from page_model.locators import OfferingsLocators #, CommonLocators


@given("The Offerings page is opened")
def step_impl(context):
    context.execute_steps(u'''
        Given The user is logged in the application
        When The user clicks the 'Offerings' on the top menu
    ''')
    # todo FIX - switching to the frame (finds the title outside the frame instead of in frame)
    # WebDriverWait(context.driver, 10).until(expected_conditions.frame_to_be_available_and_switch_to_it((By.ID, 'bzeMainIframe')))
    # title = WebDriverWait(context.driver, 5).until(expected_conditions.presence_of_element_located((By.TAG_NAME, 'title')))
    ## title = context.driver.find_element(By.XPATH, '//title[1]').text
    ## assert title.text.startswith('Sales'), "%s" % (context.driver.title)
    # assert title.text == 'Sales and Offering Space', "Page title is '%s' instead of 'Sales and Offering Space'" % (context.driver.title)
    # context.driver.switch_to.default_content()
    pass

@then("The user sees the menu with all products")
def step_impl(context):
    context.driver.switch_to_frame('bzeMainIframe')
    offerings_overview = WebDriverWait(context.driver, 10).until(expected_conditions.element_to_be_clickable(OfferingsLocators.OVERVIEW))
    assert offerings_overview.text.startswith('Overview'), "The Overview section is not present"
    context.driver.switch_to.default_content()
