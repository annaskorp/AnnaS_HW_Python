from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CalculatorPage:
    def __init__(self, driver):
        self.driver = driver
        self.url = "https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html"

        # Локаторы
        self.delay_input = (By.ID, "delay")
        self.display = (By.CLASS_NAME, "screen")
        # Локатор для кнопок по тексту (универсальный)
        self.btn_template = "//span[text()='{}']"

    def open(self):
        self.driver.get(self.url)

    def set_delay(self, seconds):
        delay = self.driver.find_element(*self.delay_input)
        delay.clear()
        delay.send_keys(seconds)

    def click_button(self, text):
        xpath = self.btn_template.format(text)
        self.driver.find_element(By.XPATH, xpath).click()

    def get_result(self, timeout):
        # Ожидаем, пока текст "15" появится в поле вывода
        WebDriverWait(self.driver, timeout).until(
            EC.text_to_be_present_in_element(self.display, "15")
        )
        return self.driver.find_element(*self.display).text
