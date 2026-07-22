from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Login Page
class LoginPage:
    def __init__(self, driver):
        self.driver = driver

    def login(self, username, password):
        self.driver.find_element(By.NAME, "username").send_keys(username)
        self.driver.find_element(By.NAME, "password").send_keys(password)
        self.driver.find_element(By.TAG_NAME, "button").click()

# Home Page
class HomePage:
    def __init__(self, driver):
        self.driver = driver

    def get_title(self):
        return self.driver.title

driver = webdriver.Chrome()
driver.get("https://the-internet.herokuapp.com/login")

login = LoginPage(driver)
login.login("tomsmith", "SuperSecretPassword!")

time.sleep(2)

home = HomePage(driver)
print("Title:", home.get_title())

driver.quit()