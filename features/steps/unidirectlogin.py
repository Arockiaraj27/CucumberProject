from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure
import pytest


@given('open chrome browser')
def launch_browser(context):
    context.driver = webdriver.Chrome(executable_path=r'C:\Automation\chromedriver.exe')
    context.driver.maximize_window()


@when('open uni homepage')
def step_impl(self):
    self.driver.get("https://demounidirectcrm.gaipp.com/signin")
    self.driver.maximize_window()


@when('Enter the username and password')
def step_impl(self):
    self.wait = WebDriverWait(self.driver, 10)
    self.wait.until(EC.presence_of_element_located((By.ID, "user"))).send_keys('admission@unidirect.org')
    self.wait.until(EC.presence_of_element_located((By.ID, "password"))).send_keys('london@2020')


@when('Click on the login button')
def step_impl(self):
    self.wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="submit"]'))).click()
    error_toast = self.wait.until(EC.presence_of_element_located((By.ID, "toast-container")))
    error_text = error_toast.text
    print(error_text)
    k = "Login Sucessfully"
    if error_text == k:
        # allure.attach(self.driver.get_screenshot_as_png(), name="create screen", attachment_type=AttachmentType.PNG)
        assert True
    else:
        self.driver.close()
        assert False
