from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# 1. Open Chrome Browser
driver = webdriver.Chrome()

# 2. Maximize Browser Window
driver.maximize_window()

# 3. Open a URL
driver.get("https://www.google.com")

# 4. Get Page Title
print("Page Title:", driver.title)

# 5. Get Current URL
print("Current URL:", driver.current_url)

# 6. Navigate to another page
driver.get("https://www.wikipedia.org")

# 7. Go Back
driver.back()
time.sleep(2)

# 8. Go Forward
driver.forward()
print("went forward")
time.sleep(2)

# 9. Refresh the Page
driver.refresh()
print("page refreshed")
time.sleep(2)

# 10. Close the Browser
driver.quit()
