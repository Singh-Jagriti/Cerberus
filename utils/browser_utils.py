# Directory: behave_cerberus/utils/browser_utils.py
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time

class BrowserUtils:
    def __init__(self):
        chrome_options = Options()
        chrome_options.add_argument("--disable-extensions")
        chrome_options.add_argument("--disable-popup-blocking")
        chrome_options.add_argument("--start-maximized")

        self.driver = webdriver.Chrome(service=Service(), options=chrome_options)

    def open_url(self, url):
        self.driver.get(url)

    def fill_form(self, name, email, current_address, permanent_address):
        self.driver.find_element(By.ID, "userName").send_keys(name)
        self.driver.find_element(By.ID, "userEmail").send_keys(email)
        self.driver.find_element(By.ID, "currentAddress").send_keys(current_address)
        self.driver.find_element(By.ID, "permanentAddress").send_keys(permanent_address)

    def submit_form(self):
        submit = self.driver.find_element(By.ID, "submit")
        self.driver.execute_script("arguments[0].scrollIntoView();", submit)
        time.sleep(1)
        self.driver.execute_script("arguments[0].click();", submit)

    def get_confirmation_name(self):
        return self.driver.find_element(By.ID, "name").text

    def close(self):
        self.driver.quit()
