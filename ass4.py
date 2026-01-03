from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Open browser
driver = webdriver.Chrome()
driver.get("https://demo.guru99.com/test/radio.html")
driver.maximize_window()

time.sleep(2)

# ---- Radio Buttons ----
radio1 = driver.find_element(By.ID, "vfb-7-1")   # Radio button 1

print("Radio1 displayed? ", radio1.is_displayed())
print("Radio1 enabled?   ", radio1.is_enabled())
print("Radio1 selected?  ", radio1.is_selected())

radio1.click()
print("Radio1 selected after click? ", radio1.is_selected())

time.sleep(1)


# ---- CheckBoxes ----
checkbox1 = driver.find_element(By.ID, "vfb-6-0")


print("\nCheckbox1 displayed? ", checkbox1.is_displayed())
print("Checkbox1 enabled?   ", checkbox1.is_enabled())
print("Checkbox1 selected?  ", checkbox1.is_selected())

checkbox1.click()
print("Checkbox1 selected after click? ", checkbox1.is_selected())



time.sleep(2)
driver.quit()
