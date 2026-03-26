'''Откройте сайт магазина: https://www.saucedemo.com/ в FireFox.
Авторизуйтесь как пользователь standard_user.
Добавьте в корзину товары:
[Sauce Labs Backpack,Sauce Labs Bolt T-Shirt,Sauce Labs Onesie]
Перейдите в корзину.
Нажмите Checkout.
Заполните форму своими данными:[имя,фамилия,почтовый индекс].
Нажмите кнопку Continue.
Прочитайте со страницы итоговую стоимость (Total).
Закройте браузер.
Проверьте, что итоговая сумма равна $58.29.'''



import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture
def driver():
    driver = webdriver.Firefox()
    driver.maximize_window()
    yield driver
    driver.quit()


def test_saucedemo_order(driver):
    wait = WebDriverWait(driver, 10)

    driver.get("https://www.saucedemo.com/")

    # 2. Авторизация
    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()

    # 3. Добавление товаров в корзину
    items_to_add = [
        "add-to-cart-sauce-labs-backpack",
        "add-to-cart-sauce-labs-bolt-t-shirt",
        "add-to-cart-sauce-labs-onesie"
    ]
    for item_id in items_to_add:
        wait.until(EC.element_to_be_clickable((By.ID, item_id))).click()

    # 4. Переход в корзину и Checkout
    driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
    wait.until(EC.element_to_be_clickable((By.ID, "checkout"))).click()

    # 5. Заполнение формы
    driver.find_element(By.ID, "first-name").send_keys("Ivan")
    driver.find_element(By.ID, "last-name").send_keys("Ivanov")
    driver.find_element(By.ID, "postal-code").send_keys("123456")
    driver.find_element(By.ID, "continue").click()

    # 6. (Total)
    # Ищем элемент, текст которого начинается с "Total: "
    total_element = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "summary_total_label")))
    total_text = total_element.text  # Получим строку вида "Total: $58.29"

    # 7. Проверка итоговой суммы
    # Проверяем, содержит ли строка нужную нам сумму
    expected_total = "Total: $58.29"
    assert total_text == expected_total, f"Ошибка! Ожидали {expected_total}, но получили {total_text}"

