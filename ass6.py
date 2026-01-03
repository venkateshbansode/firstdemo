from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Initialize WebDriver (make sure chromedriver is installed and in PATH)
driver = webdriver.Chrome()

# Open a webpage
driver.get("https://www.w3schools.com/html/html_images.asp")

# Allow some time for the page to load
time.sleep(3)
# Find all image elements
images = driver.find_elements(By.TAG_NAME, "img")
print("Found", len(images), "images")
# Loop through and print their 'src' attributes
for index, img in enumerate(images, start=1):
    src = img.get_attribute("src")
    print(f"{index}. Image URL: {src}")
# Close the browser
driver.quit()
