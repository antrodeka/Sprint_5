from selenium.webdriver.common.by import By

import locators


class TestConsruсtor:

    def test_buns_section_switch(self, driver_chrome):
        driver_chrome.find_element(By.XPATH, locators.SAUCE_BUTTON).click()
        driver_chrome.find_element(By.XPATH, locators.BUN_BUTTON).click()
        assert 'current' in driver_chrome.find_element(
            By.XPATH, locators.BUN_BUTTON).get_attribute('class')

    def test_sauces_section_switch(self, driver_chrome):
        driver_chrome.find_element(By.XPATH, locators.SAUCE_BUTTON).click()
        assert 'current' in driver_chrome.find_element(
            By.XPATH, locators.SAUCE_BUTTON).get_attribute('class')

    def test_stuff_section_switch(self, driver_chrome):
        driver_chrome.find_element(By.XPATH, locators.STUFF_BUTTON).click()
        assert 'current' in driver_chrome.find_element(
            By.XPATH, locators.STUFF_BUTTON).get_attribute('class')
