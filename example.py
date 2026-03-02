#from time import sleep
#from selenium import webdriver

#driver = webdriver.Chrome()

#driver.get("https://ya.ru/") #открывается первая страница

#driver.get("https://vk.com/") #открывается вторая страница

#driver.back()

#driver.forward()# браузер будет переходить на следующую страницу согласно истории посещения страниц

#for x in range(1, 10):
#	driver.back()
#	driver.forward()# цикл

#driver.refresh() #обновляет страницу браузера.

#driver.set_window_size(значение длины окна, значение ширины окна)

#driver.maximize_window() #открыть окно по размеру экрана
#driver.minimize_window() #свернуть окно браузера
#driver.fullscreen_window() #развернуть окно на весь экран, аналог F11

from selenium import webdriver

# Пример для Google Chrome
driver = webdriver.Chrome()
driver.get("http://www.google.com")
print(driver.title)
driver.quit()

#sleep(5)