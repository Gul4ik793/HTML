import time
from dataclasses import field

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.ie.webdriver import WebDriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC  # <-- Add this line
from webdriver_manager.drivers.edge import EdgeChromiumDriver

from extensions import get_button_classname

BASE_URL = 'http://uitestingplayground.com/'
NAMES_UNITS = {'progress_bar': 'Progress Bar'}

s = Service(r'./chromedriver.exe')

driver = webdriver.Chrome(service=s)
driver.maximize_window()
driver.get(BASE_URL)
driver.implicitly_wait(5)
time.sleep(5)
headers_section = driver.find_element(By.ID, 'overview')
headers_section.find_element(By.XPATH, f'//a[text()="{NAMES_UNITS.get('progress_bar')}"]').click()
driver.implicitly_wait(2)



button = driver.find_element(By.ID, "startButton")
button_stop = driver.find_element(By.ID, "stopButton")

button.click()

while True:
    try:
         if int(driver.find_element(By.XPATH, "//*[@aria-valuenow]").get_attribute("aria-valuenow")) == 75:
            time.sleep(1)
            button_stop.click()
            time.sleep(1)
            break
    except NoSuchElementException:
        pass

time.sleep(5)
driver.quit()
