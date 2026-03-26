#1) Нажать на кнопку
#Перейдите на страницу http://uitestingplayground.com/ajax.
#Нажмите на синюю кнопку.
#Получите текст из зеленой плашки.
#Выведите его в консоль
#("Data loaded with AJAX get request.")

from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("http://uitestingplayground.com/ajax")
ajax_button = driver.find_element(By.ID, "ajaxButton")
ajax_button.click()
wait = WebDriverWait(driver, 30)
success_message = wait.until(
    EC.presence_of_element_located((By.CSS_SELECTOR, "p.bg-success"))
)
print(success_message.text)
driver.quit()
