from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from datetime import datetime
import os
import testrail


def before_all(context):
    options = Options()
    options.headless = False
    options.add_argument('disable-gpu')
    context.driver = webdriver.Chrome(chrome_options=options)
    context.driver.get('https://ebanking-demo-ch1.ubs.com/auth/login1?userId=DEMO9999&languageCode=en')


def after_step(context, step):
    if step.status == 'failed':
        filename = context.scenario.name + "_" + datetime.now().strftime('%Y%m%d%H%M%S') + ".png"
        context.driver.save_screenshot((os.path.join(os.path.expanduser('~\\Downloads'), filename)))
        context.driver.switch_to.default_content()


# todo
def after_step(context, step):
    client = testrail.APIClient('https://ladaflac.testrail.io/')
    client.send_post('add_result/1', {'status_id': 1})
