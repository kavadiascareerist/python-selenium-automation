from selenium.webdriver.common.by import By
from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep


@given('Open Target home page')
def open_target_page(context):
    context.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    context.driver.maximize_window()
    context.driver.get('https://www.target.com/')
    sleep(10)

@when('Input tea into search button')
def clicks_search_button(context):
    sleep(5)
    search_button=context.driver.find_element(By.ID,"search") .send_keys('tea')
    search_button.click()

    search_button = context.driver.find_element(By.XPATH, "//button[@class='styles_searchButton__Mkp1S']")
    search_button.click()


@then('tea is displayed in search box')
def tea_is_displayed_in_search_box(context):
    search_button= context.driver.find_element(By.XPATH, "//button[@data-test='accountNav-signIn']")
    assert sign_in__button.is_displayed()

#

#
#
#
