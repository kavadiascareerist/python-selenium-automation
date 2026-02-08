from selenium.webdriver.common.by import By
from pages.base_page import Page


class CartPage(Page):

    empty_cart_message = (By.XPATH, "//*[contains(text(),'Your cart is empty')]")

    def is_empty_cart_message_displayed(self):
        return self.driver.find_element(*self.empty_cart_message).is_displayed()

    def open_cart_page(self):
        self.open('https://www.target.com/p/some-product-url')