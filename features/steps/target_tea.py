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

@when('clicks_search_button')
def clicks_search_button(context, search_button):
    sleep(5)
    search_button=context.driver.find_element(By.ID,"search") .send_keys('tea')
    search_in_button.click()

@then('tea is displayed')
def verify_message(context):
    search_button= context.driver.find_element(By.XPATH, "//button[@data-test='accountNav-signIn']")
    assert sign_in__button.is_displayed()

#

#
#
#
