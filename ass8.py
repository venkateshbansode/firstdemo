from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Setup Chrome
driver = webdriver.Chrome()
driver.maximize_window()

# Open page
driver.get("https://demo.automationtesting.in/Frames.html")
time.sleep(2)

# ===== 1️⃣ Switch to single iframe =====
driver.switch_to.frame("singleframe")  # iframe has name="singleframe"
print("Switched to single frame")

# Type text inside iframe
input_box = driver.find_element(By.XPATH, "//input[@type='text']")
input_box.send_keys("Hello Selenium!")
print("Typed inside single frame")

# Go back to main page
driver.switch_to.default_content()
print("Returned to main page")
time.sleep(2)

# ===== 2️⃣ Now switch to nested iframe example =====
# Click the "Iframe with in an Iframe" tab
nested_tab = driver.find_element(By.XPATH, "//a[contains(text(),'Iframe with in an Iframe')]")
nested_tab.click()
print("Opened nested iframe tab")
time.sleep(2)

# Switch to outer iframe (first)
outer_frame = driver.find_element(By.XPATH, "//iframe[@src='MultipleFrames.html']")
driver.switch_to.frame(outer_frame)
print("Switched to outer frame")

# Switch to inner iframe (second)
inner_frame = driver.find_element(By.XPATH, "//iframe[@src='SingleFrame.html']")
driver.switch_to.frame(inner_frame)
print("Switched to inner frame")

# Type inside inner frame
inner_input = driver.find_element(By.XPATH, "//input[@type='text']")
inner_input.send_keys("Hello from nested frame!")
print("Typed inside nested frame")

# Go back to parent frame (outer)
driver.switch_to.parent_frame()
print("Returned to parent (outer) frame")

# Finally go back to main page
driver.switch_to.default_content()
print("Returned to main page again")

time.sleep(2)
driver.quit()
