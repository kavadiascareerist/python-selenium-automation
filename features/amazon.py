from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

# get the path to the ChromeDriver executable
driver_path = ChromeDriverManager().install()

# create a new Chrome browser instance
service = Service(driver_path)
driver = webdriver.Chrome(service=service)
driver.maximize_window()

# open the url
driver.get('https://www.amazon.com/')
sleep(3)
driver.find_element(By.XPATH, "//i[@role='img']")
driver.find_element(By.XPATH,"input[@name='email']")
driver.find_element(By.XPATH,"input[@type='submit']")
driver.find_element(By.XPATH,"//a[@class='a-size-mini a-link-normal']")
driver.find_element(By.XPATH,"//a[@target='_blank']")
driver.find_element(By.XPATH,"//a[role='button']")
driver.find_element(By.ID,"auth-fpp-link-bottom")

