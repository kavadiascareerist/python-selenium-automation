from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Page:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        self.url = "https://www.target.com"

    cart_icon = (By.CSS_SELECTOR, "a[data-test='@web/CartLink']")

    def open(self, url):
        self.driver.get(url)

    def click(self, *locator):
        self.driver.find_element(*locator).click()

    def presence_of_element(self, *locator):
        self.wait.until(
            EC.presence_of_element_located(locator),
            message="The element is not present on the page"
        )