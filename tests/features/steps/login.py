from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


@given("The login page is opened")
def step_impl(context):
    context.driver = webdriver.Chrome('C:\Windows\Webdriver\chromedriver.exe')
    context.driver.get('https://ebanking-demo-ch1.ubs.com/auth/login1?userId=DEMO9999&languageCode=en')

@when("The user submits the prefilled contract number")
def step_impl(context):
    WebDriverWait(context.driver, 10).until(expected_conditions.element_to_be_clickable((By.NAME, 'submit'))).click()

@when("The QR code page is opened")
def step_impl(context):
    WebDriverWait(context.driver, 10).until(expected_conditions.visibility_of_element_located((By.CLASS_NAME, 'lr-qrcodetitle')))

@then("The user waits for the fake QR scan")
def step_impl(context):
    WebDriverWait(context.driver, 10).until(expected_conditions.url_changes('workbench'))

@then("The homepage is opened")
def step_impl(context):
    WebDriverWait(context.driver, 10).until(expected_conditions.frame_to_be_available_and_switch_to_it('bzeMainIframe'))
    headline = context.driver.find_element_by_xpath('/html/body/div[2]/h1[2]/span').text
    assert headline.startswith('Welcome'), "The headline doesn't start with 'Welcome'"
