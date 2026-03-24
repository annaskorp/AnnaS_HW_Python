#2) Переименовать кнопку
#Перейдите на сайт http://uitestingplayground.com/textinput.
#Укажите в поле ввода текст SkyPro.
#Нажмите на синюю кнопку.
#Получите текст кнопки и выведите в консоль ("SkyPro")


from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()
driver.get("http://uitestingplayground.com/textinput")

input_field = driver.find_element(By.ID, "newButtonName")
input_field.send_keys("SkyPro")


updating_button = driver.find_element(By.ID, "updatingButton")
updating_button.click()


print(updating_button.text)
driver.quit()

