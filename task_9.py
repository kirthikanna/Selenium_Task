from  selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
class WebpageScraper:#A class to represent a webpage scraper using selenium
    def __init__(self, url):
        self.url = url
        self.driver = None

    def setup_driver(self):
        """
        Sets up the Chrome WebDriver using Selenium WebDriver Manager.
        """
        # Use WebDriver Manager to install and manage the WebDriver
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    def fetch_webpage_content(self):#Fetches the content of the webpage
        self.driver.get(self.url)#Open the webpage
        print("Page Title:", self.driver.title)  # Print the page title
        print("Current URL:", self.driver.current_url)  # Print the current URL
        time.sleep(5)#Wait for the page to load

        # Extract the text content of the webpage
        page_content = self.driver.find_element(By.XPATH, '/html/body').text
        file = open('Webpage_task_11.txt', 'w')# Save the content to a txt file
        file.write(page_content)
        print("webpage content saved to 'Webpage_task_11.txt'")
        file.close()

def main():
    url = "https://www.saucedemo.com/"# Initialize the webpagescraper with the desired URL
    scraper = WebpageScraper(url)
    scraper.setup_driver()#set up the driver
    scraper.fetch_webpage_content()#Fetch webpage content
main()