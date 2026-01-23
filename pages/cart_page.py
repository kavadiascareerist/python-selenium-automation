from selenium.webdriver.common.by import By

class CartPage:
    def __init__(self, driver):
        self.driver = driver

    empty_cart_message = (By.XPATH, "//*[contains(text(),'Your cart is empty')]")

    def is_empty_cart_message_displayed(self):
        return self.driver.find_element(*self.empty_cart_message).is_displayed()
