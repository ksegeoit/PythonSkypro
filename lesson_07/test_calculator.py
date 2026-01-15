from selenium import webdriver
from calculator_page import CalculatorPage


def test_calculator():
    driver = webdriver.Chrome()
    url = "https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html"
    driver.get(url)
    calc = CalculatorPage(driver)
    
    calc.set_delay("45")
    calc.click_button("7")
    calc.click_button("+")
    calc.click_button("8")
    calc.click_button("=")
    
    assert calc.get_result(), "Result did not appear in time"
    driver.quit()
