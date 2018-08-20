from selenium import webdriver
from datetime import datetime
import os


def before_all(context):
    context.driver = webdriver.Chrome('C:\Windows\Webdriver\chromedriver.exe')
    context.driver.get('https://ebanking-demo-ch1.ubs.com/auth/login1?userId=DEMO9999&languageCode=en')

def after_step(context, step):
    if step.status == 'failed':
        filename = context.scenario.name + "_" + datetime.now().strftime('%Y%m%d%H%M%S') + ".png"
        context.driver.save_screenshot((os.path.join(os.path.expanduser('~\\Downloads'), filename)))
        context.driver.switch_to.default_content()
