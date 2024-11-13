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

URL = os.getenv('WEBSITE_TO_SCRAPE')
LOGIN_EMAIL = os.getenv('LOGIN_EMAIL')
LOGIN_PASSWORD = os.getenv('LOGIN_PASSWORD')

# Configure Selenium WebDriver
options = Options()
options.add_argument("--start-maximized")
driver = webdriver.Chrome(options=options)  # Specify the path if necessary, e.g., Service('path/to/chromedriver')

# Open the target URL
driver.get(URL)

# Wait for the redirection and page to fully render
wait = WebDriverWait(driver, 30)

try:
    # Locate and input email
    email_input = wait.until(EC.visibility_of_element_located((By.XPATH, "/html/body/div[3]/div/div[2]/div/div[2]/form/div[1]/input")))
    email_input.send_keys(LOGIN_EMAIL)  # Use a dummy email

    # Click the "Next" button after entering email
    next_button_email = driver.find_element(By.XPATH, "/html/body/div[3]/div/div[2]/div/div[2]/form/button")
    next_button_email.click()

    # Wait and locate password field
    password_input = wait.until(EC.visibility_of_element_located((By.XPATH, "/html/body/div[3]/div[2]/div[2]/div/div[3]/form/div[1]/input")))
    password_input.send_keys(LOGIN_PASSWORD)  # Use a dummy password

    # Click the "Next" button after entering password
    next_button_password = driver.find_element(By.XPATH, "/html/body/div[3]/div[2]/div[2]/div/div[3]/form/div[3]/button[2]")
    next_button_password.click()

    # Optional: wait for the final page to render
    time.sleep(100)  # Adjust time as necessary

finally:
    # Close the browser after completion
    driver.quit()
