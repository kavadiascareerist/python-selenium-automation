from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def click(self, locator):
        self.wait.until(EC.element_to_be_clickable(locator)).click()

    def find_element(self, locator):
        return self.wait.until(EC.presence_of_element_located(locator))

    def get_text(self, locator):
        element = self.find_element(locator)
        return element.text

class CartPage(BasePage):
    CART_ICON = (By.XPATH, "//a[@data-test='@web/CartLink']")
    EMPTY_CART_MESSAGE = (By.XPATH, "//div[contains(text(), 'Your cart is empty')]")

    def go_to_cart(self):
        self.click(self.CART_ICON)

    def is_empty_cart_message_displayed(self):
        text = self.get_text(self.EMPTY_CART_MESSAGE)
        return "Your cart is empty" in text

def test_empty_cart_message():
    driver = webdriver.Chrome()
    driver.get("https://www.target.com")
    driver.maximize_window()

    cart_page = CartPage(driver)
    cart_page.go_to_cart()

    assert cart_page.is_empty_cart_message_displayed(), "Empty cart message not shown!"

    print("Test Passed: 'Your cart is empty' message is displayed.")

    driver.quit()

if __name__ == "__main__":
    test_empty_cart_message()


