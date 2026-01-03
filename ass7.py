from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

# Setup Chrome driver
options = webdriver.ChromeOptions()
options.add_argument("--log-level=3")  # suppress warnings
driver = webdriver.Chrome(options=options)
driver.maximize_window()

# Open webpage
driver.get("https://www.automationtesting.co.uk/dropdown.html")
time.sleep(2)

# Locate dropdown
cars_menu = driver.find_element(By.XPATH, "//select[@id='cars']")
cars_menu.click()

# Create Select object
cars = Select(cars_menu)

# --- Select by visible text ---
cars.select_by_visible_text("Honda")
print("Selected by visible text: Honda")
time.sleep(2)

# --- Select by value ---
cars.select_by_value("jeep")
print("Selected by value: Jeep")
time.sleep(2)

# --- Select by index ---
cars.select_by_index(3)  # e.g., Mercedes
print("Selected by index: Mercedes")
time.sleep(2)

# --- Get all available options ---
print("\nAll available options:")
for opt in cars.options:
    print("-", opt.text)

# --- Get currently selected option ---
selected = cars.first_selected_option.text
print("\nCurrently selected:", selected)

# --- Execute JavaScript examples ---
title = driver.execute_script("return document.title;")
print("\nTitle of page:", title)

driver.execute_script("document.body.style.fontSize = '20px';")
print("Font size changed to 20px")
time.sleep(2)

driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
print("Scrolled to bottom")

# End
time.sleep(2)
driver.quit()
