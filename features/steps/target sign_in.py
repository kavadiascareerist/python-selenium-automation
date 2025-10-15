from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


@given('Open Target page home page')
def open_target(context):
    context.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    context.driver.get('https://www.target.com/')
    sleep(10)

@when('User sign in button')
def clicks_sign_in(context, sign_button):
    sleep(5)
    sign_in__button=context.driver.find_element(By.XPATH,"//button[@data-test='accountNav-signIn']")
    sign_in_button.click()

@then('User sees sign in button')
def verify_message(context):
    sign_in__button = context.driver.find_element(By.XPATH, "//button[@data-test='accountNav-signIn']")
    assert sign_in__button.is_displayed()




