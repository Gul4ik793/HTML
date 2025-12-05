import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


s = Service(r'./chromedriver.exe')

driver = webdriver.Chrome(service=s)
driver.maximize_window()
driver.get("https://ya.ru/")
driver.implicitly_wait(10)

handles = driver.window_handles
if len(handles) > 1:
    driver.switch_to.window(handles[1])
else:
    print("Открыто только одно окно")
try:
    driver.find_element(By.XPATH, '//span[text()="Сделать Яндекс поиском по умолчанию?"]')
except Exception as e:
    print("Кнопка отсутствует:", e)

driver.switch_to.window(handles[0])

search_field = driver.find_element(By.ID, 'text')
if not search_field:
    print("поле ввода отсутствует")
else:
    print("поле ввода найден")

search_field.send_keys("mail")
search_field.send_keys(Keys.ENTER)

time.sleep(5)
driver.find_element(By.TAG_NAME, "body").send_keys(Keys.ESCAPE)
time.sleep(5)

driver.find_element(By.XPATH, '//*[@id="search-result"]//li//a[contains (normalize-space(), "Облако, Календарь, Заметки, Покупки")]').click()

wait = WebDriverWait(driver, 20)
handles_now = driver.window_handles
if len(handles_now) > 1:
    driver.switch_to.window(handles_now[1])
else:
    print("Открыто только одно окно")
try:
    wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="mailbox"]//a[text()="Войти"]'))).click()
except Exception as e:
    print("Кнопка отсутствует:", e)

time.sleep(5)
driver.quit()