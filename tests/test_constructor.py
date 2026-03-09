from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

import locators


class TestConsruсtor:

    def test_buns_section_swith(self, driver_chrome):
        driver_chrome.find_element(By.XPATH, locators.SAUCE_BUTTON).click()
        driver_chrome.find_element(By.XPATH, locators.BUN_BUTTON).click()
        bun_section_title = WebDriverWait(
            driver_chrome,
            5).until(expected_conditions.visibility_of_element_located(
                (By.XPATH, locators.BUN_TITLE)))
        assert bun_section_title.is_displayed()

    def test_sauces_section_swith(self, driver_chrome):
        driver_chrome.find_element(By.XPATH, locators.SAUCE_BUTTON).click()
        sauces_section_title = WebDriverWait(driver_chrome, 5).until(
                expected_conditions.visibility_of_element_located(
                                                 (By.XPATH,
                                                  locators.SAUCE_TITLE)))
        assert sauces_section_title.is_displayed()

    def test_stuff_section_swith(self, driver_chrome):
        driver_chrome.find_element(By.XPATH, locators.STUFF_BUTTON).click()
        stuff_section_title = WebDriverWait(
            driver_chrome, 5).until(
                expected_conditions.visibility_of_element_located((
                    By.XPATH, locators.STUFF_TITLE)))
        assert stuff_section_title.is_displayed()
