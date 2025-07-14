from pages.login_page import LoginPage

def test_regression_login(browser):
    login_page = LoginPage(browser)
    login_page.go_to_login()
    login_page.login("valid@example.com", "validpass")
    assert login_page.is_login_successful()