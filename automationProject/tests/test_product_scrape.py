from pages.product_page import ProductPage

def test_scrape_products(browser):
    page = ProductPage(browser)
    page.open_products_page()
    titles = page.get_product_titles()
    assert len(titles) > 0