from locators.login_locators import *
from pages.base_page import BasePage

class LoginPage(BasePage):
    def go_to_login(self):
        from pages.home_page import HomePage
        HomePage(self.driver).go_to_login()

    def login(self, email, password):
        self.type(LOGIN_EMAIL, email)
        self.type(LOGIN_PASSWORD, password)
        self.click(LOGIN_BUTTON)

    def is_login_successful(self):
        return self.is_element_present(LOGOUT_LINK)

    def is_login_failed(self):
        return self.is_element_present(LOGIN_ERROR)