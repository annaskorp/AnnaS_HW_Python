'''Откройте страницу: https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html в Google Chrome.
В поле ввода по локатору #delay введите значение 45.
Нажмите на кнопки:7+8=
Проверьте (assert), что в окне отобразится результат 15 через 45 секунд.'''

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()


def test_slow_calculator(driver):
    # 1. Открываем страницу
    driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")

    # 2. Вводим задержку 45
    delay_input = driver.find_element(By.CSS_SELECTOR, "#delay")
    delay_input.clear()
    delay_input.send_keys("45")

    # Создаем один объект ожидания для всех действий
    wait = WebDriverWait(driver, 55)

    # 3. Нажимаем кнопки 7, +, 8, = (используем текст внутри кнопок)
    wait.until(EC.element_to_be_clickable((By.XPATH,"//span[text()='7']"))).click()
    wait.until(EC.element_to_be_clickable((By.XPATH,"//span[text()='+']"))).click()
    wait.until(EC.element_to_be_clickable((By.XPATH,"//span[text()='8']"))).click()
    wait.until(EC.element_to_be_clickable((By.XPATH,"//span[text()='=']"))).click()

    # 4. Ждем результат 15 (именно здесь сработает задержка 45 сек)
    # Метод text_to_be_present_in_element сам будет "опрашивать" экран, пока не увидит 15
    wait.until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".screen"), "15"))

    # Итоговая проверка текста на экране
    final_result = driver.find_element(By.CSS_SELECTOR, ".screen").text
    assert final_result == "15"

    print("\nПобеда! Калькулятор выдал 15.")

