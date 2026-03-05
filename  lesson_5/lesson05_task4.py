from time import sleep
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By

# Открыть браузер FireFox.
# Перейти на страницу http://the-internet.herokuapp.com/login.
# В поле username ввести значение tomsmith.
# В поле password ввести значение SuperSecretPassword!.
# Нажать кнопку Login.
# Вывести текст с зеленой плашки в консоль.
# Закрыть браузер (метод quit()).


service = Service(GeckoDriverManager().install())
driver = webdriver.Firefox(service=service)

try:
    driver.get("http://the-internet.herokuapp.com/login")

    sleep(1)  # Даем странице чуть-чуть прогрузиться
    driver.find_element(By.ID, "username").send_keys("tomsmith")
    driver.find_element(By.ID, "password").send_keys("SuperSecretPassword!")
    driver.find_element(By.CSS_SELECTOR, "button.radius").click()

    sleep(2)
    success_message = driver.find_element(By.ID, "flash").text
    print(f"Текст с плашки: {success_message}")

finally:
    sleep(5)
    driver.quit()
