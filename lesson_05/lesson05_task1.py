from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert
import time

service = Service(executable_path="drivers/chromedriver.exe")
driver = webdriver.Chrome(service=service)

try:
    driver.get("http://uitestingplayground.com/classattr")
    blue_button = driver.find_element(By.CSS_SELECTOR, "button.btn-primary")
    blue_button.click()
    Alert(driver).accept()
    print("Успешный клик! Задание 1 выполнено.")
    time.sleep(2)
finally:
    driver.quit()
