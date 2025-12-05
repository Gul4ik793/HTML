import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


s = Service(r'./chromedriver.exe')

driver = webdriver.Chrome(service=s)
driver.maximize_window()
driver.get("https://demoqa.com/text-box")
driver.implicitly_wait(10)

driver.find_element(By.ID, 'userName').send_keys("Хасанова")
time.sleep(2)

driver.find_element(By.ID, 'userEmail').send_keys("123@mail.ru")
time.sleep(2)

driver.find_element(By.ID, 'currentAddress').send_keys("Уфа")
time.sleep(2)

driver.find_element(By.ID, 'permanentAddress').send_keys("Уфа")
time.sleep(2)

driver.find_element(By.ID, "submit").click()
time.sleep(5)

driver.quit()