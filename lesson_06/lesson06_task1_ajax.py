from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def task1_ajax():
    driver = webdriver.Chrome()
    driver.get("http://uitestingplayground.com/ajax")

    driver.find_element(By.ID, "ajaxButton").click()

    label = WebDriverWait(driver, 15).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "p.bg-success"))
    )
    print(label.text)

    driver.quit()


if __name__ == "__main__":
    task1_ajax()
