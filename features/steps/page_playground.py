from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def click(self, locator):
        self.wait.until(EC.element_to_be_clickable(locator)).click()

    def find_element(self, locator):
        return self.wait.until(EC.presence_of_element_located(locator))

    def verify_text(self, locator, expected_text):
        element = self.find_element(locator)
        actual_text = element.text
        assert expected_text in actual_text, f'Expected "{expected_text}" but got "{actual_text}"'


class CartPage(BasePage):
    CART_ICON = (By.CSS_SELECTOR, '[data-test="@web/CartIcon"]')
    EMPTY_MESSAGE = (By.XPATH, '//h1[contains(text(),"Your cart is empty")]')

    def open_cart(self):
        self.click(self.CART_ICON)

    def verify_empty_cart_message(self):
        self.verify_text(self.EMPTY_MESSAGE, "Your cart is empty")


driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.maximize_window()
driver.get("https://www.target.com/")

cart_page = CartPage(driver)
cart_page.open_cart()
cart_page.verify_empty_cart_message()

print("✅ Test passed: 'Your cart is empty' message verified.")


