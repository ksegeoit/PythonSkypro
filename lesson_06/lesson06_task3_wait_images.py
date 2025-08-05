from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def task3_wait_images():
    driver = webdriver.Chrome()
    url = "https://bonigarcia.dev/selenium-webdriver-java/loading-images.html"
    driver.get(url)
    
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "image-container"))
    )
    
    images = driver.find_elements(By.CSS_SELECTOR, "#image-container img")
    print(images[2].get_attribute("src"))
    
    driver.quit()


if __name__ == "__main__":
    task3_wait_images()
