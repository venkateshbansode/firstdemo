from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import time
driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.selenium.dev/")  # Example website
driver.implicitly_wait(10)
print(" Implicit Wait: Waiting up to 10 seconds for elements to be found")
try:
    element = driver.find_element(By.LINK_TEXT, "Projects")
    print(" Found element using implicit wait:", element.text)
except Exception as e:
    print("Element not found using implicit wait:", e)
print("\n Explicit Wait: Waiting until a specific condition is true")
try:
    wait = WebDriverWait(driver, 10)  
    element = wait.until(
        EC.presence_of_element_located((By.LINK_TEXT, "Documentation"))
    )
    print(" Found element using explicit wait:", element.text)
except TimeoutException:
    print("Element not found using explicit wait within time limit")
print("\n Fluent Wait: Custom polling frequency and ignored exceptions")
try:
    fluent_wait = WebDriverWait(driver, timeout=20, poll_frequency=2, ignored_exceptions=[TimeoutException])
    element = fluent_wait.until(
        EC.visibility_of_element_located((By.LINK_TEXT, "Support")))
    print("Found element using fluent wait:", element.text)
except TimeoutException:
    print("Element not found using fluent wait within time limit")
time.sleep(2)
driver.quit()
print("\n Test Completed")
