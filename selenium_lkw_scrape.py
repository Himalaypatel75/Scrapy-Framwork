from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time
import os
from dotenv import load_dotenv

load_dotenv()

URL_LKW = os.getenv('URL_LKW')
LOGIN_EMAIL_LKW = os.getenv('LOGIN_EMAIL_LKW')
LOGIN_PASSWORD_LKW = os.getenv('LOGIN_PASSWORD_LKW')

# Configure Selenium WebDriver
options = Options()
options.add_argument("--start-maximized")
driver = webdriver.Chrome(options=options)  # Specify the path if necessary, e.g., Service('path/to/chromedriver')

# Open the URL
driver.get(URL_LKW)

# Wait for the page to load
wait = WebDriverWait(driver, 20)

try:
    # Locate and input email
    email_input = wait.until(EC.visibility_of_element_located((By.XPATH, "/html/body/div[2]/div/div/div/div/div/div[1]/form/div[1]/div/div/input")))
    email_input.send_keys(LOGIN_EMAIL_LKW)  # Use a dummy email

    # Locate and input password
    password_input = wait.until(EC.visibility_of_element_located((By.XPATH, "/html/body/div[2]/div/div/div/div/div/div[1]/form/div[2]/div/div/input")))
    password_input.send_keys(LOGIN_PASSWORD_LKW)  # Use a dummy password

    # Click the "Login" button
    login_button = driver.find_element(By.XPATH, "/html/body/div[2]/div/div/div/div/div/div[1]/form/div[4]/input[2]")
    login_button.click()

    # Wait for 20 seconds after login
    time.sleep(20)

finally:
    # Close the browser after completion
    driver.quit()