import asyncio
import os
from dotenv import load_dotenv
from pyppeteer import launch
from pyppeteer.errors import NetworkError, TimeoutError

load_dotenv()

URL_SENNDER = os.getenv('URL_SENNDER')
LOGIN_EMAIL_SENNDER = os.getenv('LOGIN_EMAIL_SENNDER')
LOGIN_PASSWORD_SENNDER = os.getenv('LOGIN_PASSWORD_SENNDER')

async def main():
    # Launch the browser
    browser = await launch(headless=False, args=['--start-maximized', '--disable-popup-blocking'])

    # Open a new tab
    page = await browser.newPage()

    # Set the preferences to allow cookies
    await page.setCookie({
        'name': 'cookieConsent',
        'value': 'true',
        'domain': 'app.orcas.sennder.com'
    })

    # Go to the Sennder login URL
    await page.goto(URL_SENNDER)

    try:
        # Wait for the cookie consent popup and accept it
        await page.waitForSelector('button.cookie-accept', {'timeout': 5000})
        await page.click('button.cookie-accept')

        # Wait for the email input to be visible and type the email
        await page.waitForSelector("input[type='email']")
        await page.type("input[type='email']", LOGIN_EMAIL_SENNDER)

        # Wait for the password input to be visible and type the password
        await page.waitForSelector("input[type='password']")
        await page.type("input[type='password']", LOGIN_PASSWORD_SENNDER)

        # Locate and click the login button
        await page.waitForSelector("button[type='submit']")
        await page.click("button[type='submit']")

        # Optionally wait for some time after login (e.g., for redirection)
        await page.waitFor(2000)  # 2 seconds wait

    except (TimeoutError, NetworkError) as e:
        print(f"Error occurred: {e}")
    
    finally:
        # Close the browser
        await browser.close()

# Run the async main function
asyncio.get_event_loop().run_until_complete(main())
