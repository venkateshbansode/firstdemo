from selenium import webdriver
import time

driver = webdriver.Chrome()
# Open a local or web page
driver.get("https://www.google.com")  
driver.maximize_window()
time.sleep(2)
# ----- Window Size -----
print("Current Size:", driver.get_window_size())
driver.set_window_size(800, 600)
print("New Size:", driver.get_window_size())
time.sleep(2)
# ----- Window Position -----
print("Current Position:", driver.get_window_position())
driver.set_window_position(100, 100)
print("New Position:", driver.get_window_position())
time.sleep(2)

# ----- Open New Window -----
driver.execute_script("window.open('https://www.python.org','_blank');")
time.sleep(2)

# Get all window handles
all_windows = driver.window_handles
print("All Windows:", all_windows)

# Switch to new window
driver.switch_to.window(all_windows[1])
print("Switched to New Window Title:", driver.title)
time.sleep(2)
driver.close()  # Close new window

# Switch back to main window
driver.switch_to.window(all_windows[0])
print("Back to Main Window Title:", driver.title)

driver.quit()
print(" Simple window handling demo completed!")
