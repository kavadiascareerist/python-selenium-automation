from selenium.webdriver.common.by import By

class HomePage:
    def __init__(self, driver):
        self.driver = driver
        self.url = "https://www.target.com"

    cart_icon = (By.CSS_SELECTOR, "a[data-test='@web/CartLink']")

    def open(self):
        self.driver.get(self.url)

    def click_cart(self):
        self.driver.find_element(*self.cart_icon).click()
