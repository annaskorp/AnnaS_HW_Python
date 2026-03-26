'''1.Откройте страницу: https://bonigarcia.dev/selenium-webdriver-java/data-types.html в Edge или Safari.
2.Заполните форму значениями:
3.Нажмите кнопку Submit.
4.Проверьте (assert), что поле Zip code подсвечено красным.
5.Проверьте (assert), что остальные поля подсвечены зеленым.'''

import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest


@pytest.fixture
def driver():
    # Используем os для надежного пути к драйверу
    current_dir = os.path.dirname(os.path.abspath(__file__))
    driver_path = os.path.join(current_dir, "msedgedriver.exe")

    service = EdgeService(executable_path=driver_path)
    driver = webdriver.Edge(service=service)
    driver.maximize_window()
    yield driver
    driver.quit()


def test_form_validation(driver):
    wait = WebDriverWait(driver, 10)
    driver.get("https://bonigarcia.dev/selenium-webdriver-java/data-types.html")

    first_name = wait.until(EC.element_to_be_clickable((By.NAME, "first-name")))
    first_name.send_keys("Иван")

    driver.find_element(By.NAME, "last-name").send_keys("Иванов")
    driver.find_element(By.NAME, "address").send_keys("Ленина, 1")
    driver.find_element(By.NAME, "e-mail").send_keys("test@example.com")
    driver.find_element(By.NAME, "phone").send_keys("+79001234567")
    driver.find_element(By.NAME, "city").send_keys("Москва")
    driver.find_element(By.NAME, "country").send_keys("Россия")
    driver.find_element(By.NAME, "job-position").send_keys("QA")
    driver.find_element(By.NAME, "company").send_keys("Skypro")

    # Нажимаем Submit
    driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

    # Проверка Zip code (красный)
    zip_code = driver.find_element(By.ID, "zip-code")
    assert "alert-danger" in zip_code.get_attribute("class")

    # Проверка остальных полей (зеленые)
    fields = ["first-name", "last-name", "address", "e-mail", "phone", "city", "country", "job-position", "company"]
    for field_id in fields:
        element = driver.find_element(By.ID, field_id)
        assert "alert-success" in element.get_attribute("class")






