from behave import given, when, then
# from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from page_model.locators import CommonLocators


@given("The application page is loaded")
def step_impl(context):
    WebDriverWait(context.driver, 10).until(expected_conditions.text_to_be_present_in_element(CommonLocators.APP_NAME, "Digital Banking"))

@when("The user closes the welcome message")
def step_impl(context):
    WebDriverWait(context.driver, 10).until(expected_conditions.element_to_be_clickable(CommonLocators.WELCOME_MSG)).click()

@then("The user lands on the homepage")
def step_impl(context):
    WebDriverWait(context.driver, 10).until_not(expected_conditions.presence_of_element_located(CommonLocators.WELCOME_MSG))
    page_title = context.driver.find_element(*CommonLocators.PAGE_TITLE)
    assert page_title.text == 'Account and custody account overview', 'Tag h2 = {}'.format(page_title.text)



# login removed from the application

# @given("The login page is opened")
# def step_impl(context):
#     assert context.driver.find_element(By.CLASS_NAME, 'uwr-keyline'), "Title 'Login' not found"

# @when("The user submits the prefilled contract number")
# def step_impl(context):
#     WebDriverWait(context.driver, 10).until(expected_conditions.element_to_be_clickable((By.NAME, 'submit'))).click()

# @when("The QR code page is opened")
# def step_impl(context):
#     WebDriverWait(context.driver, 10).until(expected_conditions.visibility_of_element_located((By.CLASS_NAME, 'lr-qrcodetitle')))

# @then("The user waits for the fake QR scan")
# def step_impl(context):
#     WebDriverWait(context.driver, 10).until(expected_conditions.url_changes('workbench'))

# @then("The homepage is opened")
# def step_impl(context):
#     WebDriverWait(context.driver, 10).until(expected_conditions.frame_to_be_available_and_switch_to_it(CommonLocators.MAIN_IFRAME))
#     headline = context.driver.find_element(By.XPATH, '/html/body/div[2]/h1[2]/span').text
#     context.driver.switch_to.default_content()
#     assert headline.startswith('Welcome'), "The headline doesn't start with 'Welcome'"
