from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Используем автоматическое управление драйверами
driver = webdriver.Firefox()

try:
    driver.get("http://the-internet.herokuapp.com/inputs")
    input_field = driver.find_element(By.CSS_SELECTOR, "input[type='number']")
    input_field.send_keys("Sky")
    time.sleep(1)
    input_field.clear()
    time.sleep(1)
    input_field.send_keys("Pro")
    print("Поле заполнено! Задание 3 выполнено.")
    time.sleep(2)
finally:
    driver.quit()
