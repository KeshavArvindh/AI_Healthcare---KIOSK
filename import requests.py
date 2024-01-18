import selenium
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options
import smtplib
from bs4 import BeautifulSoup
import random

from selenium import webdriver

# Set the path to your ChromeDriver executable
service = Service(executable_path='C:/Users/adith/Downloads/chromedriver-win32/chromedriver-win32/chromedriver.exe')

# Set the URL you want to open
url = 'https://www.makemytrip.com/'

# Set the path to your Chrome profile directory
chrome_profile_directory = 'C:\\Users\\adith\\AppData\\Local\\Google\\Chrome\\User Data\Default'

# Create ChromeOptions
options = webdriver.ChromeOptions()
options.add_argument(f'user-data-dir={chrome_profile_directory}')

# Start a new Chrome WebDriver instance with the specified profile
driver = webdriver.Chrome(service=service, options=options)

# Open the specified URL
driver.get(url)

# Find and interact with login elements
try:
    # Click the login button by CSS selector
    driver.find_element_by_id('username').click()

    # Enter username and password and click the login button
    driver.find_element_by_id('username').send_keys('hustler.av@gmail.com')
    driver.find_element_by_id('password').send_keys('mmt@2023')
    driver.find_element_by_id('login-button').click()
except Exception as e:
    print(f"An error occurred: {e}")

# Optional: Add a delay to observe the page
input("Press Enter to exit...")

# Close the WebDriver when you're done
driver.quit()


# chrome_options = Options()
# chrome_options.add_experimental_option("detach", True)

# class Browser:
#     browser, service = None, None

#     def __init__(self, driver: str):
#         self.service = Service(driver)
#         self.browser = webdriver.Chrome(service=self.service, options=chrome_options)
#         self.wait = WebDriverWait(self.browser, 10)

#     def open_page(self, url: str):
#         self.browser.get(url)
#         self.browser.maximize_window()

#     def close_browser(self):
#         self.browser.close()

#     def add_input(self, by: By, value: str, text: str):
#         try:
#             field = self.wait.until(EC.presence_of_element_located((by, value)))
#             field.send_keys(text)
#             time.sleep(1)
#         except selenium.common.exceptions.TimeoutException:
#             print(f"Element not found: {by}, {value}")

#     def click_button(self, by: By, value: str):
#         try:
#             button = self.wait.until(EC.element_to_be_clickable((by, value)))
#             button.click()
#             time.sleep(1)
#         except selenium.common.exceptions.TimeoutException:
#             print(f"Element not clickable: {by}, {value}")

#     def login(self, username: str, password: str):
#         self.add_input(by=By.ID, value='mat-input-2', text=username)
#         self.add_input(by=By.ID, value='mat-input-3', text=password)

#     def oneinput(self, tex: str, val: str):
#         self.add_input(by=By.XPATH, value=val, text=tex)

#     def exec_script(self, by: By, path: str):
#         element_to_scroll_to = self.browser.find_element(by, path)
#         self.browser.execute_script("arguments[0].scrollIntoView();", element_to_scroll_to)
#         time.sleep(2)

#     def scrollup(self):
#         self.browser.execute_script("window.scrollTo(0, 0)")

#     def scrolldown(self):
#         self.browser.execute_script("window.scrollTo(0,document.body.scrollHeight")

# if __name__ == '__main__':
#     browser = Browser(r'C:/Users/adith/Downloads/chromedriver-win32/chromedriver-win32/chromedriver.exe')
#     browser.open_page('https://www.makemytrip.com/')
#     chrome_profile_directory = "/path/to/your/chrome/profile"

# # Create ChromeOptions
#     chrome_options = webdriver.ChromeOptions()
#     chrome_options.add_argument(f"user-data-dir={chrome_profile_directory}")

# # Start a new Chrome WebDriver instance with the specified profile
#     driver = webdriver.Chrome(executable_path='/path/to/chromedriver', chrome_options=chrome_options)

#     time.sleep(3)
#     browser.click_button(By.CSS_SELECTOR, '.makeFlex.hrtlCenter.font10.makeRelative.lhUser.userLoggedOut')
#     browser.click_button(By.CSS_SELECTOR, "#username")
#     browser.login("hustler.av@gmail.com", "mmt@2023")
#     time.sleep(6)

    # ... (continue with your code)

# # Function to scrape flight ticket prices
# def scrape_flight_prices():
    

#     # Open the website


    
    

#     # Use BeautifulSoup to    parse the webpage
#     soup = BeautifulSoup(driver.page_source, "html.parser")

#     # Extract flight ticket price information
#     # Modify this part based on the specific website's HTML structure
#     price_element = soup.find("span", class_="flight-price")
#     if price_element:
#         ticket_price = price_element.text.strip()
#         return ticket_price
#     else:
#         return None

# # Function to send an email
# def send_email(subject, message):
#     # Replace these variables with your email configuration
#     sender_email = "akhilarayalaa@gmail.com"
#     sender_password = "password"
#     receiver_email = "reddyhashish@gmail.com"

#     # Create an SMTP connection
#     server = smtplib.SMTP("smtp.gmail.com", 587)
#     server.starttls()
#     server.login(sender_email, sender_password)

#     # Create the email message
#     email_message = f"Subject: {subject}\n\n{message}"

#     # Send the email
#     server.sendmail(sender_email, receiver_email, email_message)

#     # Close the SMTP connection
#     server.quit()

# if __name__ == "__main__":
#     ticket_price = scrape_flight_prices()
    

#     if ticket_price:
#         subject = "Flight Ticket Price Alert"
#         message = f"The current ticket price is: {ticket_price}"

#         send_email(subject, message)
#         print("Email sent successfully.")
#     else:
#         print("Ticket price not found.")