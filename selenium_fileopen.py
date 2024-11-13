from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium.webdriver.common.by import By

# Path to your custom Chrome browser
chrome_path = "/usr/bin/google-chrome"

# Set Chrome options to use the custom path and specific user profile
options = Options()
options.binary_location = chrome_path  # Set the binary location
options.add_argument('--no-sandbox')  # Disable sandboxing for Linux environments
options.add_argument('--disable-dev-shm-usage')  # Helps with memory issues
options.add_argument('--disable-gpu')  # Disable GPU acceleration (optional)
# options.add_argument('--remote-debugging-port=9222')  # Debugging port for Chrome
# options.add_argument('--headless')  # Use headless mode (optional, if you want it to run without UI)

# Set the path to your Chrome user profile
user_data_dir = "/home/himalay/.config/google-chrome"  # Adjust this path
profile_name = "Profile 1"  # Replace with the profile you want to use (e.g., "Default", "Profile 1")

options.add_argument(f"--user-data-dir={user_data_dir}")
options.add_argument(f"--profile-directory={profile_name}")

# Initialize WebDriver with Service
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)

# Open the GitHub URL
url = "https://github.com/Himalaypatel75?tab=repositories"
driver.get(url)

# Wait for the page to load
time.sleep(5)  # Alternatively, use WebDriverWait for a more robust solution

# Get all text content on the page
page_text = driver.find_element(By.TAG_NAME, "body").text
print(page_text)  # Print all visible text content on the page
time.sleep(20)  # Keep the page open for a while

# Close the browser
driver.quit()
