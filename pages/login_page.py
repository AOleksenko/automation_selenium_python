from support.base_methods import BaseMethods
import config

input_username = "//input[@name='UserName']"
input_password = "//input[@name='Password']"
btn_login = ".//*[@class='btn btn-primary']"


class LoginPage(BaseMethods):
    def __init__(self, driver):
        super().__init__(driver)

    def perform_login_operation(self):
        self.driver.get(config.app_url)
        self.wait_until_element_displayed(btn_login)
        self.find(input_username).send_keys(config.user_name)
        self.find(input_password).send_keys(config.password)
        self.find(btn_login).click()