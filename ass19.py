from selenium import webdriver
import time

# Launch Chrome browser
driver = webdriver.Chrome()

# Open a webpage
driver.get("https://www.python.org")
driver.maximize_window()

time.sleep(2)

# Scroll down by pixels
driver.execute_script("window.scrollBy(0, 500);")  # scroll down 500 pixels
time.sleep(2)

# Scroll up by pixels
driver.execute_script("window.scrollBy(0, -300);")  # scroll up 300 pixels
time.sleep(2)

# Scroll to the bottom of the page
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
time.sleep(2)

# Scroll back to the top
driver.execute_script("window.scrollTo(0, 0);")
time.sleep(2)
driver.quit()
