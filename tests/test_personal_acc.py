from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

import locators


class TestPersonalAccount:

    def test_personal_acc_button_from_main_page_pers_acc_page_open(
            self, driver_with_login_user):
        driver_with_login_user.find_element(By.XPATH,
                                            locators.PERSONAL_ACCOUNT).click()
        WebDriverWait(
            driver_with_login_user,
            5).until(expected_conditions.visibility_of_element_located(
                (By.XPATH, locators.LOGOUT_BUTTON)))
        assert "profile" in driver_with_login_user.current_url

    def test_constructor_button_from_personal_acc_constructor_open(
            self, driver_with_login_user):
        driver_with_login_user.find_element(
            By.XPATH, locators.PERSONAL_ACCOUNT).click()
        WebDriverWait(driver_with_login_user, 5).until(
            expected_conditions.visibility_of_element_located(
                (By.XPATH, locators.LOGOUT_BUTTON)))
        driver_with_login_user.find_element(
            By.XPATH, locators.CONSTRUCTOR_BUTTON).click()
        order_button = WebDriverWait(
            driver_with_login_user, 5).until(
                expected_conditions.visibility_of_element_located(
                    (By.XPATH, locators.ORDER_BUTTON)))
        assert order_button.is_displayed()

    def test_logo_button_from_personal_acc_constructor_open(
            self, driver_with_login_user):
        driver_with_login_user.find_element(
            By.XPATH, locators.PERSONAL_ACCOUNT).click()
        WebDriverWait(driver_with_login_user, 5).until(
            expected_conditions.visibility_of_element_located(
                (By.XPATH, locators.LOGOUT_BUTTON)))
        driver_with_login_user.find_element(
            By.XPATH, locators.LOGO_STELLAR_BURGERS).click()
        order_button = WebDriverWait(
            driver_with_login_user, 5).until(
                expected_conditions.visibility_of_element_located(
                    (By.XPATH, locators.ORDER_BUTTON)))
        assert order_button.is_displayed()

    def test_logout_from_personal_acc_login_form_open(
            self, driver_with_login_user):
        driver_with_login_user.find_element(
            By.XPATH, locators.PERSONAL_ACCOUNT).click()
        WebDriverWait(driver_with_login_user, 5).until(
            expected_conditions.visibility_of_element_located(
                (By.XPATH, locators.LOGOUT_BUTTON))).click()
        WebDriverWait(driver_with_login_user, 5).until(
            expected_conditions.visibility_of_element_located(
                (By.XPATH, locators.LOGIN_BUTTON)))
        assert "login" in driver_with_login_user.current_url
