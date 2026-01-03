from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Launch browser
driver = webdriver.Chrome()
driver.get("https://www.example.com")  # Any website you want
driver.maximize_window()

time.sleep(2)  # Wait for page to load completely

# 1️ Full Page Screenshot
driver.save_screenshot("full_page.png")
print(" Full page screenshot saved as 'full_page.png'")

# 2️ Screenshot of a Specific Element
element = driver.find_element(By.TAG_NAME, "h1")  # Example: first <h1> element
element.screenshot("element_screenshot.png")
print(" Element screenshot saved as 'element_screenshot.png'")

# Close browser
driver.quit()
