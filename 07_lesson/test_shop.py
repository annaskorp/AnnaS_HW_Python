from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
import pytest
from selenium import webdriver
from pages import LoginPage, InventoryPage, CartPage, CheckoutPage


def test_saucedemo_purchase():
    # Использование Firefox
    # Скачаем нужный geckodriver и запустиМ Firefox
    driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))

    driver.implicitly_wait(10)  # Неявное ожидание для стабильности


    # 1. Авторизация
    driver.get("https://www.saucedemo.com/")
    login_pg = LoginPage(driver)
    login_pg.login("standard_user", "secret_sauce")

    # 2. Добавление товаров и переход в корзину
    inv_pg = InventoryPage(driver)
    inv_pg.add_items()
    inv_pg.go_to_cart()

    # 3. Переход к оформлению
    cart_pg = CartPage(driver)
    cart_pg.checkout()

    # 4. Заполнение данных и проверка цены
    check_pg = CheckoutPage(driver)
    check_pg.fill_form("Susy", "Gray", "123456")

    total_text = check_pg.get_total()

    # Проверка (Assert)
    assert "58.29" in total_text, f"Ожидалось $58.29, но получили {total_text}"


    driver.quit()
