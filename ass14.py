from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Open local demo file
driver = webdriver.Chrome()
driver.get("file:///C:/Python/demo_gmail.html")  # Change path if needed
driver.maximize_window()

# Step 1: Enter email and password
driver.find_element(By.XPATH, "//input[contains(@type,'email')]").send_keys("test@gmail.com")
driver.find_element(By.XPATH, "//input[contains(@type,'password')]").send_keys("test123")
driver.find_element(By.XPATH, "//button[contains(text(),'Next')]").click()
time.sleep(1)

# Step 2: Compose email
driver.find_element(By.XPATH, "//textarea[contains(@id,'to')]").send_keys("friend@mail.com")
driver.find_element(By.XPATH, "//input[contains(@id,'subject')]").send_keys("Demo Email")
driver.find_element(By.XPATH, "//textarea[contains(@id,'message')]").send_keys("This is a test email using Selenium.")
driver.find_element(By.XPATH, "//button[contains(text(),'Send')]").click()

print("Email Sent Successfully in Demo Page!")
driver.quit()
