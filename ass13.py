from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
import time

# 1. Setup WebDriver
driver = webdriver.Chrome()
driver.maximize_window()

# 2. Open website containing tooltip
driver.get("https://seleniumbase.io/demo_page")
time.sleep(3)

# 3. Locate the element that has a tooltip
tooltip_element = driver.find_element(By.ID, "myTooltip")

# 4. Hover over the element to make tooltip visible
action = ActionChains(driver)
action.move_to_element(tooltip_element).perform()
time.sleep(2)

# 5. Get the tooltip text (from the 'title' attribute)
tooltip_text = tooltip_element.get_attribute("title")

# 6. Verify tooltip text
expected_tooltip = "This is a tooltip for the text input below."
if tooltip_text == expected_tooltip:
    print("✅ Tooltip verification passed! Tooltip text:", tooltip_text)
else:
    print("❌ Tooltip verification failed!")
    print("Expected:", expected_tooltip)
    print("Found:", tooltip_text)

# 7. Close browser
time.sleep(2)
driver.quit()
