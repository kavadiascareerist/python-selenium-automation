from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep


@given("User is on target home page")
def open_target(context):
    context.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    context.driver.maximize_window()
    context.driver.get("https://www.target.com/")
    sleep(3)


@when("user search item")
def search_product(context):
    search_button = context.driver.find_element(By.ID, "search")
    search_button.send_keys("coffe")
    search_button = context.driver.find_element(By.XPATH,"//button[@aria-label='search']")
    search_button.click()
    sleep(3)

@when("user adds item to the cart")
def add_item_to_cart(context):
    add_item_to_cart = context.driver.find_element(By.ID,"addToCartButtonOrTextIdFor13397813").click()

    sleep(5)


@then("user should see item in the cart")
def verify_cart(context):
    cart_button = context.driver.find_element(By.CSS_SELECTOR, "a[data-test='cart-icon']")
    cart_button.click()
    sleep(2)  # wait for cart page
    cart_items = context.driver.find_elements(By.XPATH,"//use[@href='/icons/Cart.svg#Cart']")
    assert len(cart_items) > 0, "No items found in the cart"
    print(f"Number of items in cart: {len(cart_items)}")

    context.driver.quit()
