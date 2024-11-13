from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time
import os
import pickle
from dotenv import load_dotenv

load_dotenv()

URL_SENNDER = os.getenv('URL_SENNDER')
LOGIN_EMAIL_SENNDER = os.getenv('LOGIN_EMAIL_SENNDER')
LOGIN_PASSWORD_SENNDER = os.getenv('LOGIN_PASSWORD_SENNDER')


# Configure Selenium WebDriver
options = Options()
options.add_argument("--start-maximized")
options.add_argument("--disable-popup-blocking")

# Add preference to automatically accept cookies (for Chrome)
prefs = {
    "profile.default_content_setting_values.cookies": 1,  # 1 allows cookies, 2 blocks cookies
    "profile.managed_default_content_settings.cookies": 1  # Ensures cookies are allowed for all sites
}
options.add_experimental_option("prefs", prefs)

driver = webdriver.Chrome(options=options)  # Specify the path if necessary, e.g., Service('path/to/chromedriver')

# Open the Orcas Sennder login URL

cookies = pickle.load(open("cookies.pkl", "rb"))
# print(cookies)
for cookie in cookies:
    # cookie['domain'] = "app.orcas.sennder.com"
    try:
        cookie.pop("expiry", None)
        driver.add_cookie(cookie)
    except:
        pass
# # Wait for the page to load and be ready
# wait = WebDriverWait(driver, 30)

# # Capture the HTML content before interacting with the page
# html_content_before = driver.page_source

# # Save the HTML content into a file before rendering
# with open("page_before_render.html", "w", encoding="utf-8") as file:
#     file.write(html_content_before)

# Wait for 5 seconds to allow rendering
time.sleep(2)
driver.get(URL_SENNDER)
time.sleep(5)
# print(driver.get_cookies())
# pickle.dump(driver.get_cookies(), open("cookies.pkl", "wb"))

# print("wait completed")

# # Capture the HTML content after waiting for the page to render
# html_content_after = driver.page_source

# # Save the HTML content into a file after rendering
# with open("page_after_render.html", "w", encoding="utf-8") as file:
#     file.write(html_content_after)

wait = WebDriverWait(driver, 30)
time.sleep(5)
# Now that the content is rendered, we proceed with the next step
try:

    modal = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "dsf-modal-2-115-0[data-test='cookies-modal']")))

    # Locate the "Continue without accepting" link inside the modal
    continue_button = modal.find_element(By.CSS_SELECTOR, "dsf-link-2-115-0.w-fit")

    # Click on the "Continue without accepting" link
    continue_button.click()
    time.sleep(5)

        
    # Capture the HTML content before interacting with the page
    html_content_before = driver.page_source

    # Save the HTML content into a file before rendering
    with open("old_page_before_render.html", "w", encoding="utf-8") as file:
        file.write(html_content_before)

    login_email_model = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "dsf-input-4-14-1[data-test='login-email']")))
    login_email_model.send_keys(LOGIN_EMAIL_SENNDER)


    login_password_model = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "dsf-input-4-14-1[data-test='login-password']")))
    login_password_model.send_keys(LOGIN_PASSWORD_SENNDER)

    login_model = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "dsf-button-4-14-1[data-test='login-button']")))
    login_model.click()

    # Optionally wait for 20 seconds after login to allow for any processing
    time.sleep(20)

finally:
    # Close the browser after completion
    driver.quit()
