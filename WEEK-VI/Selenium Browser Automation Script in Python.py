from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

driver.get("https://www.google.com")
driver.maximize_window()

search = driver.find_element(By.NAME, "q")
search.send_keys("Selenium Python")
search.submit()

time.sleep(3)

print("Page Title:", driver.title)

driver.quit()