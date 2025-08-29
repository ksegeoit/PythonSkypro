import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture
def browser():
    driver = webdriver.Edge()
    yield driver
    driver.quit()


def test_form_validation(browser):
    url = "https://bonigarcia.dev/selenium-webdriver-java/data-types.html"
    browser.get(url)

    fields = {
        "first-name": "Иван",
        "last-name": "Петров",
        "address": "Ленина, 55-3",
        "e-mail": "test@skypro.com",
        "phone": "+7985899998787",
        "zip-code": "",
        "city": "Москва",
        "country": "Россия",
        "job-position": "QA",
        "company": "SkyPro"
    }

    # Заполняем форму по атрибуту name вместо id
    for field_name, value in fields.items():
        browser.find_element(By.NAME, field_name).send_keys(value)

    browser.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

    # Проверяем подсветку поля Zip code (должно быть красным)
    zip_code = WebDriverWait(browser, 10).until(
        EC.visibility_of_element_located((By.NAME, "zip-code"))
    )
    assert "alert-danger" in zip_code.get_attribute("class") or "is-invalid" in zip_code.get_attribute("class")

    # Проверяем подсветку остальных полей (должны быть зелеными)
    valid_fields = [
        "first-name", "last-name", "address", "e-mail",
        "phone", "city", "country", "job-position", "company"
    ]
    for field_name in valid_fields:
        field = browser.find_element(By.NAME, field_name)
        assert "alert-success" in field.get_attribute("class") or "is-valid" in field.get_attribute("class")