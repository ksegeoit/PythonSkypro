from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

service = Service(executable_path="drivers/chromedriver.exe")
driver = webdriver.Chrome(service=service)

try:
    driver.get("http://uitestingplayground.com/dynamicid")
    blue_button = driver.find_element(By.CSS_SELECTOR, "button.btn-primary")
    blue_button.click()
    print("Успешный клик! Задание 2 выполнено.")
    time.sleep(2)
finally:
    driver.quit()
