from selenium import webdriver
from selenium.webdriver.common.by import By


def task2_rename_button():
    driver = webdriver.Chrome()
    driver.get("http://uitestingplayground.com/textinput")
    
    input_field = driver.find_element(By.ID, "newButtonName")
    input_field.send_keys("SkyPro")
    
    driver.find_element(By.ID, "updatingButton").click()
    
    button = driver.find_element(By.ID, "updatingButton")
    print(button.text)
    
    driver.quit()


if __name__ == "__main__":
    task2_rename_button()
