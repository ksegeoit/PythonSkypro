from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Используем автоматическое управление драйверами
driver = webdriver.Firefox()

try:
    driver.get("http://the-internet.herokuapp.com/login")
    driver.find_element(By.ID, "username").send_keys("tomsmith")
    driver.find_element(By.ID, "password").send_keys("SuperSecretPassword!")
    driver.find_element(By.CSS_SELECTOR, "button.radius").click()
    message = driver.find_element(By.ID, "flash").text
    cleaned_message = message.split("\n")[0]
    print(f"Сообщение системы: {cleaned_message}")
    print("Задание 4 выполнено.")
    time.sleep(3)
finally:
    driver.quit()
