import time

def test_performance_products(browser):
    start = time.time()
    browser.get("https://automationexercise.com/products")
    duration = time.time() - start
    assert duration < 5