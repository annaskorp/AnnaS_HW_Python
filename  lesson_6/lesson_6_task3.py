#3) Дождаться картинки
#Перейдите на сайт https://bonigarcia.dev/selenium-webdriver-java/loading-images.html.
#Дождитесь загрузки всех картинок.
#Получите значение атрибута src у 3-й картинки.
#Выведите значение в консоль.

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()

driver.get("https://bonigarcia.dev/selenium-webdriver-java/loading-images.html")

wait = WebDriverWait(driver, 20)
third_image = wait.until(
    EC.presence_of_element_located((By.XPATH, "(//img)[3]"))
)

src_value = third_image.get_attribute("src")

print(f"URL 3-й картинки: {src_value}")

driver.quit()
