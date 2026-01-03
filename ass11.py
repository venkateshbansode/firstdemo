# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
import time

# 1. Setup WebDriver
driver = webdriver.Chrome()
driver.maximize_window()

# 2. Open website containing tooltip demo
driver.get("https://jqueryui.com/tooltip/")
time.sleep(3)

# 3. Switch to the iframe that contains the tooltip example
driver.switch_to.frame(driver.find_element(By.CLASS_NAME, "demo-frame"))
time.sleep(3)
# 4. Locate the input box that has a tooltip
input_box = driver.find_element(By.ID, "age")
time.sleep(3)
# 5. Hover over the input box to trigger tooltip
action = ActionChains(driver)
action.move_to_element(input_box).perform()
time.sleep(2)

# 6. Get tooltip text (tooltip is shown in a div with role='tooltip')
tooltip_text = driver.find_element(By.CLASS_NAME, "ui-tooltip-content").text
time.sleep(3)
# 7. Verify tooltip text
expected_tooltip = "We ask for your age only for statistical purposes."
time.sleep(3)
if tooltip_text == expected_tooltip:
    print("Tooltip verification passed!")
    print("Tooltip text:", tooltip_text)
else:
    print("Tooltip verification failed!")
    print("Expected:", expected_tooltip)
    print("Found:", tooltip_text)

# 8. Close browser
time.sleep(2)
driver.quit()
