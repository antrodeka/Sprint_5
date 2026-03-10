import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

from variables import (USER_EMAIL,
                       USER_PASS_6_SIMB,
                       URL_MAIN_PAGE)
import locators


@pytest.fixture(scope="function")
def driver_chrome():
    driver = webdriver.Chrome()
    driver.get(URL_MAIN_PAGE)
    yield driver
    driver.quit()


@pytest.fixture(scope="function")
def driver_with_login_user(driver_chrome):
    driver_chrome.find_element(By.XPATH, locators.LOGIN_IN_ACCOUNT).click()
    driver_chrome.find_element(By.XPATH,
                               locators.LOGIN_EMAIL).send_keys(USER_EMAIL)
    driver_chrome.find_element(
        By.XPATH, locators.LOGIN_PASSWORD).send_keys(
                                       USER_PASS_6_SIMB)
    driver_chrome.find_element(By.XPATH, locators.LOGIN_BUTTON).click()
    WebDriverWait(
            driver_chrome,
            5).until(expected_conditions.visibility_of_element_located(
                (By.XPATH,
                 locators.ORDER_BUTTON)))
    return driver_chrome
