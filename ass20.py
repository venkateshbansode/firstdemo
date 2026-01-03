from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time
driver = webdriver.Chrome()
driver.maximize_window()
# ====== Right Click Example ======
driver.get("https://swisnl.github.io/jQuery-contextMenu/demo.html")
time.sleep(2)
actions = ActionChains(driver)
# Locate the button to right-click
right_click_btn = driver.find_element(By.CSS_SELECTOR, ".context-menu-one.btn.btn-neutral")
# Perform right-click
print("Performing Right Click...")
actions.context_click(right_click_btn).perform()
time.sleep(2)
# Select 'Edit' option from the context menu
edit_option = driver.find_element(By.CSS_SELECTOR, ".context-menu-icon-edit")
edit_option.click()
time.sleep(1)
# Handle alert
alert = driver.switch_to.alert
print("Alert Text:", alert.text)
alert.accept()
time.sleep(2)
# ====== Double Click Example ======
driver.get("https://demo.guru99.com/test/simple_context_menu.html")
time.sleep(3)
# Locate the double-click button
dbl_click_btn = driver.find_element(By.XPATH, "//button[text()='Double-Click Me To See Alert']")
print("Performing Double Click...")
actions.double_click(dbl_click_btn).perform()
time.sleep(2)
# Handle double-click alert
alert = driver.switch_to.alert
print("Alert Text:", alert.text)
alert.accept()
time.sleep(1)
driver.quit()
print("Double click and right click actions completed successfully!")
