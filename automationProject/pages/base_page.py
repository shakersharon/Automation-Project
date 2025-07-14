class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def click(self, locator):
        self.driver.find_element(*locator).click()

    def type(self, locator, value):
        self.driver.find_element(*locator).send_keys(value)

    def is_element_present(self, locator):
        return len(self.driver.find_elements(*locator)) > 0