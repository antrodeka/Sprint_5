from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

from variables import (USER_NAME,
                       USER_PASS_6_SIMB,
                       USER_PASS_5_SIMB)
import locators
from conftest import generate_login


class TestRegistration:

    def test_reg_name_not_empty_email_right_pass_more_then_6_simb_acc_created(
            self,
            driver_chrome):
        driver_chrome.find_element(By.XPATH, locators.PERSONAL_ACCOUNT).click()
        driver_chrome.find_element(By.XPATH,
                                   locators.REG_BUTTON_ON_LOGIN_PAGE).click()
        test_email = generate_login()
        driver_chrome.find_element(By.XPATH,
                                   locators.REG_NAME_INPUT
                                   ).send_keys(USER_NAME)
        driver_chrome.find_element(By.XPATH, 
                                   locators.REG_EMAIL_INPUT
                                   ).send_keys(test_email)
        driver_chrome.find_element(By.NAME,
                                   locators.REG_PASSWORD_INPUT
                                   ).send_keys(USER_PASS_6_SIMB)
        driver_chrome.find_element(By.XPATH, locators.REG_BUTTON).click()
        login_button = WebDriverWait(driver_chrome, 5).until(
            expected_conditions.visibility_of_element_located((
                By.XPATH, locators.LOGIN_BUTTON)))
        assert login_button.is_displayed()

    def test_reg_name_not_empty_email_right_pass_less_then_6_simb_error(
            self,
            driver_chrome):
        driver_chrome.find_element(By.XPATH, locators.PERSONAL_ACCOUNT).click()
        driver_chrome.find_element(By.XPATH,
                                   locators.REG_BUTTON_ON_LOGIN_PAGE).click()
        test_email = generate_login()
        driver_chrome.find_element(By.XPATH,
                                   locators.REG_NAME_INPUT
                                   ).send_keys(USER_NAME)
        driver_chrome.find_element(By.XPATH, 
                                   locators.REG_EMAIL_INPUT
                                   ).send_keys(test_email)
        driver_chrome.find_element(By.NAME,
                                   locators.REG_PASSWORD_INPUT
                                   ).send_keys(USER_PASS_5_SIMB)        
        driver_chrome.find_element(By.XPATH, locators.REG_BUTTON).click()
        error_title = WebDriverWait(driver_chrome, 5).until(
            expected_conditions.visibility_of_element_located(
                (By.XPATH, locators.ERROR_PASS_MESSAGE)))
        assert error_title.is_displayed()
