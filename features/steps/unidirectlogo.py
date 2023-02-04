from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure
import pytest

@given('I launch chrome browser')
def step_impl(context):
    context.driver = webdriver.Chrome(executable_path=r'C:\Automation\chromedriver.exe')
    context.driver.maximize_window()
    assert True


@when('I open the uni CRM Signin page')
def step_impl(context):
    context.driver.get("https://demounidirectcrm.gaipp.com/")
    assert True


@when('Enter the username "{user}" and password "{pwd}"')
def step_impl(context, user, pwd):
    context.wait = WebDriverWait(context.driver, 10)
    context.wait.until(EC.presence_of_element_located((By.ID, "user"))).send_keys(user)
    context.wait.until(EC.presence_of_element_located((By.ID, "password"))).send_keys(pwd)
    assert True


@when('Click the login button')
def step_impl(context):
    context.wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="submit"]'))).click()
    assert True


@then('user must login into the dashboard page successfully')
def step_impl(context):
    logo = context.driver   .find_element_by_xpath("//li[contains(text(),'Dashboard home')]").is_visible()
    assert logo is True
    context.driver.close()





