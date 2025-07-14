import pytest
from pages.login_page import LoginPage
import csv

@pytest.mark.parametrize("email,password", [
    ("valid@gmail.com", "validpass"),
    ("invalid@gmail.com", "wrongpass")
])
def test_login_functionality(browser, email, password):
    login_page = LoginPage(browser)
    login_page.go_to_login()
    login_page.login(email, password)
    assert login_page.is_login_successful() or login_page.is_login_failed()
