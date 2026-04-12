from selenium.webdriver.common.by import By

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.username_field = (By.ID, "user-name")
        self.password_field = (By.ID, "password")
        self.login_button = (By.ID, "login-button")

    def login(self, user, pwd):
        self.driver.find_element(*self.username_field).send_keys(user)
        self.driver.find_element(*self.password_field).send_keys(pwd)
        self.driver.find_element(*self.login_button).click()

class InventoryPage:
    def __init__(self, driver):
        self.driver = driver
        # Универсальный локатор для добавления в корзину по ID товара
        self.add_to_cart_btns = {
            "backpack": (By.ID, "add-to-cart-sauce-labs-backpack"),
            "t-shirt": (By.ID, "add-to-cart-sauce-labs-bolt-t-shirt"),
            "onesie": (By.ID, "add-to-cart-sauce-labs-onesie")
        }
        self.cart_link = (By.CLASS_NAME, "shopping_cart_link")

    def add_items(self):
        for item in self.add_to_cart_btns.values():
            self.driver.find_element(*item).click()

    def go_to_cart(self):
        self.driver.find_element(*self.cart_link).click()

class CartPage:
    def __init__(self, driver):
        self.driver = driver
        self.checkout_btn = (By.ID, "checkout")

    def checkout(self):
        self.driver.find_element(*self.checkout_btn).click()

class CheckoutPage:
    def __init__(self, driver):
        self.driver = driver
        self.first_name = (By.ID, "first-name")
        self.last_name = (By.ID, "last-name")
        self.zip_code = (By.ID, "postal-code")
        self.continue_btn = (By.ID, "continue")
        self.total_label = (By.CLASS_NAME, "summary_total_label")

    def fill_form(self, f_name, l_name, zip_c):
        self.driver.find_element(*self.first_name).send_keys(f_name)
        self.driver.find_element(*self.last_name).send_keys(l_name)
        self.driver.find_element(*self.zip_code).send_keys(zip_c)
        self.driver.find_element(*self.continue_btn).click()

    def get_total(self):
        # Извлекаем текст вида "Total: $58.29"
        return self.driver.find_element(*self.total_label).text
