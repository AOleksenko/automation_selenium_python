from support.base_methods import BaseMethods

navbar = "//nav[contains(@class, 'navbar')]"
nav_link_home = navbar + "//a[contains(.,'Home')]"
nav_link_schedules = navbar + "//a[contains(.,'Schedules')]"
nav_link_destinations = navbar + "//a[contains(.,'Destinations')]"
nav_link_data = navbar + "//a[contains(.,'Data')]"
nav_link_analytics = navbar + "//a[contains(.,'Analytics')]"
nav_link_user_info = navbar + "//a[@class = 'nav-link dropdown-toggle pl-3']"
dd_option_logout = "//a[text()= 'Logout']"


class HomePage(BaseMethods):
    def __init__(self, driver):
        super().__init__(driver)

    def check_basic_elements_on_page(self):
        self.wait_until_element_displayed(nav_link_home)
        assert self.find(nav_link_schedules).is_displayed
        assert self.find(nav_link_destinations).is_displayed
        assert self.find(nav_link_data).is_displayed
        assert self.find(nav_link_analytics).is_displayed

    def perform_logout_operation(self):
        self.wait_until_element_clickable(nav_link_user_info)
        self.find(nav_link_user_info).click()
        self.wait_until_element_has_attribute(nav_link_user_info, "aria-expanded", "true")
        self.find(dd_option_logout).click()