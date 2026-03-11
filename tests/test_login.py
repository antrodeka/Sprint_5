from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

from variables import (USER_EMAIL,
                       USER_PASS_6_SIMB)
import locators


class TestLogin:

    def test_login_from_main_page_login_success(self, driver_chrome):
        driver_chrome.find_element(By.XPATH, locators.LOGIN_IN_ACCOUNT).click()
        driver_chrome.find_element(By.XPATH,
                                   locators.LOGIN_EMAIL).send_keys(USER_EMAIL)
        driver_chrome.find_element(By.XPATH,
                                   locators.LOGIN_PASSWORD).send_keys(
                                       USER_PASS_6_SIMB)
        driver_chrome.find_element(By.XPATH, locators.LOGIN_BUTTON).click()
        assert WebDriverWait(
            driver_chrome,
            5).until(expected_conditions.visibility_of_element_located(
                (By.XPATH,
                 locators.ORDER_BUTTON))).is_displayed()

    def test_login_from_personal_account_login_success(self, driver_chrome):
        driver_chrome.find_element(By.XPATH, locators.PERSONAL_ACCOUNT).click()
        driver_chrome.find_element(By.XPATH,
                                   locators.LOGIN_EMAIL).send_keys(USER_EMAIL)
        driver_chrome.find_element(
            By.XPATH, locators.LOGIN_PASSWORD).send_keys(USER_PASS_6_SIMB)
        driver_chrome.find_element(By.XPATH, locators.LOGIN_BUTTON).click()
        assert WebDriverWait(driver_chrome, 5).until(
            expected_conditions.visibility_of_element_located(
                (By.XPATH, locators.ORDER_BUTTON))).is_displayed()

    def test_login_from_reg_form_success_login(self, driver_chrome):
        driver_chrome.find_element(By.XPATH, locators.LOGIN_IN_ACCOUNT).click()
        driver_chrome.find_element(By.XPATH,
                                   locators.REG_BUTTON_ON_AUTH_PAGE).click()
        driver_chrome.find_element(By.XPATH,
                                   locators.RESET_PASSWORD_LOGIN_BUTTON).click()
        driver_chrome.find_element(By.XPATH,
                                   locators.LOGIN_EMAIL).send_keys(USER_EMAIL)
        driver_chrome.find_element(
            By.XPATH, locators.LOGIN_PASSWORD).send_keys(USER_PASS_6_SIMB)
        driver_chrome.find_element(By.XPATH, locators.LOGIN_BUTTON).click()
        assert WebDriverWait(
            driver_chrome,
            5).until(expected_conditions.visibility_of_element_located(
                (By.XPATH, locators.ORDER_BUTTON))).is_displayed()

    def test_login_from_pass_reset_form_success_login(self, driver_chrome):
        driver_chrome.find_element(By.XPATH, locators.LOGIN_IN_ACCOUNT).click()
        driver_chrome.find_element(By.XPATH,
                                   locators.RESTORE_PASSWORD_BUTTON).click()
        driver_chrome.find_element(
            By.XPATH, locators.RESET_PASSWORD_LOGIN_BUTTON).click()
        driver_chrome.find_element(
            By.XPATH, locators.LOGIN_EMAIL).send_keys(USER_EMAIL)
        driver_chrome.find_element(
            By.XPATH, locators.LOGIN_PASSWORD).send_keys(USER_PASS_6_SIMB)
        driver_chrome.find_element(By.XPATH, locators.LOGIN_BUTTON).click()
        assert WebDriverWait(
            driver_chrome,
            5).until(expected_conditions.visibility_of_element_located(
                (By.XPATH, locators.ORDER_BUTTON))).is_displayed()
