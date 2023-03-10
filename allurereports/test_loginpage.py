import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from allure_commons.types import AttachmentType
import allurereports
import allure


class Test:
    @allure.severity(allure.severity_level.MINOR)
    def test_logo(self):
        self.driver = webdriver.Chrome(executable_path=r"C:\Users\sakth\Desktop\Automation\chromedriver.exe")
        self.driver.get("https://demounidirectcrm.gaipp.com/signin")
        self.driver.maximize_window()
        title = self.driver.title

        if title == "UniDirect":
            self.driver.close()
            assert True
        else:
            self.driver.close()

    @allure.severity(allure.severity_level.CRITICAL)
    def test_login(self):
        self.driver = webdriver.Chrome(executable_path=r"C:\Users\sakth\Desktop\Automation\chromedriver.exe")
        self.driver.get("https://demounidirectcrm.gaipp.com/signin")
        self.driver.maximize_window()
        self.wait = WebDriverWait(self.driver, 10)
        self.wait.until(EC.presence_of_element_located((By.ID, "user"))).send_keys('drunkard@gmail.com')
        self.wait.until(EC.presence_of_element_located((By.ID, "password"))).send_keys('24356')
        self.wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="submit"]'))).click()
        error_toast = self.wait.until(EC.presence_of_element_located((By.ID, "toast-container")))
        error_text = error_toast.text
        print(error_text)
        m = "Entered wrong username or password, please check it"
        if error_text == m:
            allure.attach(self.driver.get_screenshot_as_png(), name="Login screen", attachment_type=AttachmentType.PNG)
            assert True
        else:
            self.driver.close()
            assert False

    @allure.severity(allure.severity_level.CRITICAL)
    def test_same(self):
        self.driver = webdriver.Chrome(executable_path=r"C:\Users\sakth\Desktop\Automation\chromedriver.exe")
        self.driver.get("https://demounidirectcrm.gaipp.com/signin")
        self.driver.maximize_window()
        self.wait = WebDriverWait(self.driver, 10)
        self.wait.until(EC.presence_of_element_located((By.ID, "user"))).send_keys('admission@unidirect.org')
        self.wait.until(EC.presence_of_element_located((By.ID, "password"))).send_keys('london')
        self.wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="submit"]'))).click()
        error_toast = self.wait.until(EC.presence_of_element_located((By.ID, "toast-container")))
        error_text = error_toast.text
        print(error_text)
        k = "Logged in successfully"
        if error_text == k:
            allure.attach(self.driver.get_screenshot_as_png(), name="create screen", attachment_type=AttachmentType.PNG)
            assert True
        else:
            self.driver.close()
            assert False
