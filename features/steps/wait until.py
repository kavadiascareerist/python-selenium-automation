
from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager


@given('user open Target home page')
def open_target_page(context):
    context.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    context.driver.maximize_window()
    context.driver.get('https://www.target.com/')

    # Wait until search box is visible before proceeding
    wait = WebDriverWait(context.driver, 15)
    wait.until(EC.visibility_of_element_located((By.ID, 'search')))


@when('put tea into search button')
def input_search_text(context):
    wait = WebDriverWait(context.driver, 10)

    search_box = wait.until(EC.element_to_be_clickable((By.ID, 'search')))
    search_box.clear()
    search_box.send_keys('tea')

    search_icon = wait.until(
        EC.element_to_be_clickable((By.XPATH, "//button[@data-test='@web/Search/SearchButton']"))
    )
    search_icon.click()

    wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "div[data-test='resultsGrid']")))


@then('tea is in search box')
def tea_is_in_search_box(context):
    wait = WebDriverWait(context.driver, 10)
    search_box = wait.until(EC.visibility_of_element_located((By.ID, 'search')))
    value = search_box.get_attribute('value')

    assert 'tea' in value.lower(), f"Expected 'tea' in search box, but got '{value}'"
    print(" tea  is displayed correctly in the search box")

    context.driver.quit()
