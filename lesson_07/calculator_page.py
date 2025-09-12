from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CalculatorPage:
    def __init__(self, driver):
        self.driver = driver
        self.delay_input = (By.CSS_SELECTOR, "#delay")
        self.result_screen = (By.CLASS_NAME, "screen")
        self.buttons = {
            "7": (By.XPATH, "//span[text()='7']"),
            "+": (By.XPATH, "//span[text()='+']"),
            "8": (By.XPATH, "//span[text()='8']"),
            "=": (By.XPATH, "//span[text()='=']")
        }

    def set_delay(self, delay):
        self.driver.find_element(*self.delay_input).clear()
        self.driver.find_element(*self.delay_input).send_keys(delay)

    def click_button(self, button):
        self.driver.find_element(*self.buttons[button]).click()

    def get_result(self):
        return WebDriverWait(self.driver, 46).until(
            EC.text_to_be_present_in_element(self.result_screen, "15")
        )
