from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

#Открыть браузер Google Chrome.
#Перейти на страницу: http://uitestingplayground.com/dynamicid.
#Кликнуть на синюю кнопку.



driver = webdriver.Chrome()
driver.get("http://uitestingplayground.com/dynamicid")
driver.find_element(By.CSS_SELECTOR, "button.btn-primary").click()

sleep(5)