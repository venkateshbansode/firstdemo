from selenium import webdriver
from selenium.webdriver.common.by import By
import requests
import time

driver = webdriver.Chrome()
driver.get("https://www.w3schools.com/")
driver.maximize_window()
time.sleep(2)

# ---- By ID ----
link1 = driver.find_element(By.ID, "navbtn_exercises")
print("By ID href:", link1.get_attribute("href"))

# ---- By Link Text ----
link2 = driver.find_element(By.LINK_TEXT, "Learn HTML")
print("By Text href:", link2.get_attribute("href"))

# ---- By Partial Link Text ----
link3 = driver.find_element(By.PARTIAL_LINK_TEXT, "Learn")
print("By Partial Text href:", link3.get_attribute("href"))

# ---- By XPath ----
link4 = driver.find_element(By.XPATH, "//a[text()='Learn CSS']")
print("By XPath href:", link4.get_attribute("href"))

# ---- Check if hyperlink is valid ----
url = link2.get_attribute("href")
response = requests.head(url)
if response.status_code == 200:
    print(" [ok] Valid Link :", url)
else:
    print("[Broken] Link :", url)

driver.quit()
