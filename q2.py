from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

# Setup Chrome with WebDriver Manager (auto driver download)
driver = webdriver.Chrome()
driver.maximize_window()
# Open a sample login page (demo site)
driver.get("https://www.saucedemo.com/")
time.sleep(3)
# --- TextBox Example ---
# Enter username
driver.find_element(By.ID, "user-name").send_keys("standard_user")
time.sleep(3)
# Enter password
driver.find_element(By.NAME, "password").send_keys("secret_sauce")
time.sleep(3)
# --- Button Example ---
# Click the Login button
driver.find_element(By.ID, "login-button").click()

time.sleep(3)  # wait to see the result

# --- SendKeys with Keys Example ---
# Search bar not available here, but for example:
# driver.find_element(By.ID, "search").send_keys("Selenium" + Keys.RETURN)

# Close browser
driver.quit()
