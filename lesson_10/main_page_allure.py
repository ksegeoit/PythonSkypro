from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver


class MainPage:
    """Класс для работы с главной страницей."""
    
    def __init__(self, driver: WebDriver) -> None:
        """
        Инициализация главной страницы.
        
        :param driver: WebDriver instance
        """
        self.driver = driver
    
    def add_first_item_to_cart(self) -> None:
        """Добавление первого товара в корзину."""
        self.driver.find_element(By.CLASS_NAME, "btn_inventory").click()
    
    def go_to_cart(self) -> None:
        """Переход в корзину."""
        self.driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()