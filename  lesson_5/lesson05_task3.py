from time import sleep
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By

#Открыть браузер FireFox.
#Перейти на страницу: http://the-internet.herokuapp.com/inputs.
#Ввести в поле текст Sky.
#Очистить это поле (метод clear()).
#Ввести в поле текст Pro.
#Закрыть браузер (метод quit()).


service = Service(GeckoDriverManager().install())
driver = webdriver.Firefox(service=service)

try:
    driver.get("http://the-internet.herokuapp.com/inputs")
    sleep(3)

    input_field = driver.find_element(By.TAG_NAME, "input")

    # --- меняем тип поля с 'number' на 'text' ---
    driver.execute_script("arguments[0].setAttribute('type', 'text')", input_field)
    # ------------------------------------------------------

    input_field.send_keys("Sky")
    sleep(3)

    input_field.clear()
    sleep(3)

    input_field.send_keys("Pro")
    sleep(3)

finally:
    driver.quit()

