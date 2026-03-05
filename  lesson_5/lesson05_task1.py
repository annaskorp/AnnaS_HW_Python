#Открыть браузер Google Chrome.
#Перейти на страницу: http://uitestingplayground.com/classattr.
#Кликнуть на синюю кнопку.

from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("http://uitestingplayground.com/classattr")
blue_button = driver.find_element(By.XPATH,
                                  "//button[contains(concat(' ', normalize-space(@class), ' '), ' btn-primary ')]")
blue_button.click()

sleep(5)

