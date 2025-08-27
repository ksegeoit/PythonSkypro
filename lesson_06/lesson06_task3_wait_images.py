from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def task3_wait_images():
    driver = webdriver.Chrome()
    url = "https://bonigarcia.dev/selenium-webdriver-java/loading-images.html"
    driver.get(url)
    
    # Ожидаем загрузку элемента с id="award"
    WebDriverWait(driver, 30).until(
        EC.presence_of_element_located((By.ID, "award"))
    )
    
    # Получаем элемент с id="award"
    award = driver.find_element(By.ID, "award")
    print("URL 3-й картинки:", award.get_attribute("src"))
    
    driver.quit()


if __name__ == "__main__":
    task3_wait_images()

