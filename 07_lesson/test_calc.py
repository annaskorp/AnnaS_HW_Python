import pytest
from selenium import webdriver
from calc_page import CalculatorPage


@pytest.fixture
def driver():
    # Инициализация
    browser = webdriver.Chrome()
    browser.implicitly_wait(5)
    yield browser
    # Закрытие после завершения теста
    browser.quit()


@pytest.fixture
def calc(driver):
    return CalculatorPage(driver)


def test_slow_calculator(calc):
    # 1. Открываем страницу
    calc.open()

    # 2. Вводим задержку 45
    calc.set_delay("45")

    # 3. Нажимаем 7 + 8 =
    calc.click_button("7")
    calc.click_button("+")
    calc.click_button("8")
    calc.click_button("=")

    # 4. Проверяем результат (timeout внутри метода должен поддерживать явное ожидание)
    result = calc.get_result(timeout=50)

    assert result == "15", f"Ожидалось 15, но получили {result}"
