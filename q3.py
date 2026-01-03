from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
# 1. Open Chrome browser
driver = webdriver.Chrome()

# 2. Open Google website
driver.get("https://www.google.com")
time.sleep(3)
# 3. Find the search box
search_box = driver.find_element(By.NAME, "q")

# 4. Type text into search box
search_box.send_keys("Selenium")
time.sleep(4)


# 6. Wait and then close the browser
driver.quit()