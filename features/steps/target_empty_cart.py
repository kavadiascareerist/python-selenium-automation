from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

@when('user open target ')
def open_target(context):
    context.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    context.driver.maximize_window()
    context.driver.get('https://www.target.com/')
    sleep(5)


@when('User clicks on cart button')
def clicks_cart(context):
    sleep(3)
    cart_button=context.driver.find_element(By.CSS_SELECTOR,'[data-test="@web/CartLink"]')
    cart_button.click()

@then('User sees a message " your cart is empty"')
def verify_message(context):
    sleep(5)
    message=context.driver.find_element(By.XPATH,"//div[@data-test='boxEmptyMsg']").text
    assert "Your cart is empty" in message, f"Expected message: 'Your cart is empty' not found. Found:{message}"


