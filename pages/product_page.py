from pages.base_page import BasePage

class ProductPage(BasePage):
    def open_products_page(self):
        self.driver.find_element("link text", "Products").click()

    def get_product_titles(self):
        return [p.text for p in self.driver.find_elements("xpath", "//div[@class='productinfo text-center']/p")]