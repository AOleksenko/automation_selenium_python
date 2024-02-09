from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BaseMethods:
    def __init__(self, driver):
        self.driver = driver

    def find(self, xpath):
        return self.driver.find_element(By.XPATH, xpath)

    def wait_until_element_displayed(self, xpath):
        wait = WebDriverWait(self.driver, 30)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, xpath)
            )
        )

    def wait_until_element_clickable(self, xpath):
        wait = WebDriverWait(self.driver, 30)
        wait.until(
            EC.element_to_be_clickable(
                (By.XPATH, xpath)
            )
        )

    def wait_until_element_has_attribute(self, xpath, attribute, value):
        wait = WebDriverWait(self.driver, 30)
        # element = f"{xpath}[(contains(@{attribute},'{value}'))]"
        # wait.until(EC.presence_of_element_located((By.XPATH, element)))
        wait.until(
            EC.text_to_be_present_in_element_attribute(
                (By.XPATH, xpath),
                attribute,
                value
            )
        )