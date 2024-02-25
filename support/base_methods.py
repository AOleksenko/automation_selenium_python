from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BaseMethods:
    def __init__(self, driver):
        self.driver = driver
        self.wait_timeout = 30

    def find(self, xpath):
        return self.driver.find_element(By.XPATH, xpath)

    def wait_until(self, condition, xpath, attribute=None, value=None):
        wait = WebDriverWait(self.driver, self.wait_timeout)
        locator = (By.XPATH, xpath)

        if attribute and value:
            wait.until(condition(locator, attribute, value))
        else:
            wait.until(condition(locator))

    def wait_until_element_displayed(self, xpath):
        self.wait_until(EC.presence_of_element_located, xpath)

    def wait_until_element_clickable(self, xpath):
        self.wait_until(EC.element_to_be_clickable, xpath)

    def wait_until_element_has_attribute(self, xpath, attribute, value):
        # element = f"{xpath}[(contains(@{attribute},'{value}'))]"
        # wait.until(EC.presence_of_element_located((By.XPATH, element)))
        self.wait_until(EC.text_to_be_present_in_element_attribute, xpath, attribute, value)