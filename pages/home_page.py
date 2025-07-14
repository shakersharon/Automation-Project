from locators.home_locators import HOME_LOGIN_BUTTON
from pages.base_page import BasePage

class HomePage(BasePage):
    def go_to_login(self):
        self.click(HOME_LOGIN_BUTTON)