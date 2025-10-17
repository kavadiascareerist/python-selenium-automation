from behave import given, then
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

@given("user opens the Target Circle page")
def open_target_circle_page(context):
    context.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    context.driver.maximize_window()
    context.driver.get("https://www.target.com/circle")
    sleep(5)

@then("the page display at least 10 benefit cells")
def verify_benefit_cells(context):
    benefit_cells = context.driver.find_elements(By.XPATH,"//h1[text()='Target Circle™']")
    assert len(benefit_cells) >= 10
    print(f"Found {len(benefit_cells)} benefit cells.")


