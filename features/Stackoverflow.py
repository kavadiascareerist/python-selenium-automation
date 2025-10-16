from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

# get the path to the ChromeDriver executable
driver_path = ChromeDriverManager().install()

# create a new Chrome browser instance
service = Service(driver_path)
drive = webdriver.Chrome(service=service)
driver.maximize_window()

driver.get('https://stackoverflow.com/users/signup')
driver.find_element(By.XPATH, "//h1[text()='Create your account']")
driver.find_element(By.XPATH,"//div[@class='flex--item js-terms fs-caption fc-black-400 ta-left']")
driver.find_element(By.ID,"email")
driver.find_element(By.ID,"password")
driver.find_element(By.ID,"submit-button")
driver.find_element(By.XPATH,"//button[@data-provider='google']")
driver.find_element(By.XPATH,"//button[@data-provider='github']")
driver.find_element(By.XPATH,"//svg[@aria-hidden='true']")

