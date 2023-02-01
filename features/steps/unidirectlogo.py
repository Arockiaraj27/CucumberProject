from behave import *
from selenium import webdriver


@given('Launch chrome browser')
def launch_browser(context):
    context.driver = webdriver.Chrome(executable_path=r'C:\Automation\chromedriver.exe')
    context.driver.maximize_window()


@when('open orange hrm homepage')
def open_homepage(context):
    context.driver.get("https://demounidirectcrm.gaipp.com/")


@then('verify that the logo present on page')
def verify_logo(context):
    status=context.driver.find_element_by_xpath("//*[@id='submit']").is_displayed()
    assert status is True


@then('close browser')
def close_browser(context):
    context.driver.close()
