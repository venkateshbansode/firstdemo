from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Initialize the Chrome WebDriver
driver = webdriver.Chrome()

# Open a demo page for alerts
driver.get("https://the-internet.herokuapp.com/javascript_alerts")
driver.maximize_window()

# Wait for page to load
time.sleep(2)

# ---------- Example 1: Simple Alert ----------
driver.find_element(By.XPATH, "//button[text()='Click for JS Alert']").click()
time.sleep(1)

# Switch to alert and accept
alert = driver.switch_to.alert
print("Alert Text:", alert.text)
alert.accept()
print("Simple Alert Accepted.\n")

# ---------- Example 2: Confirmation Alert ----------
driver.find_element(By.XPATH, "//button[text()='Click for JS Confirm']").click()
time.sleep(1)

alert = driver.switch_to.alert
print("Confirmation Alert Text:", alert.text)
alert.dismiss()   # Click 'Cancel'
print("Confirmation Alert Dismissed.\n")

# ---------- Example 3: Prompt Alert ----------
driver.find_element(By.XPATH, "//button[text()='Click for JS Prompt']").click()
time.sleep(1)

alert = driver.switch_to.alert
print("Prompt Alert Text:", alert.text)
alert.send_keys("Selenium Test")
alert.accept()
print("Prompt Alert Accepted with Input.\n")

time.sleep(2)

# ---------- Example 4: Popup Window Handling ----------
driver.get("https://demo.automationtesting.in/Windows.html")
time.sleep(3)

# Click button to open a new window
driver.find_element(By.XPATH, "//button[contains(text(),'click')]").click()
time.sleep(3)

# Get window handles
handles = driver.window_handles
main_window = driver.current_window_handle

# Switch to the new window
for handle in handles:
    if handle != main_window:
        driver.switch_to.window(handle)
        print("Popup Window Title:", driver.title)
        driver.close()

# Switch back to main window
driver.switch_to.window(main_window)
print("Back to main window.")

# Close browser
driver.quit()
