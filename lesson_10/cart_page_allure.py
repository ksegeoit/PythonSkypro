from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver


class CartPage:
    """Класс для работы со страницей корзины."""
    
    def __init__(self, driver: WebDriver) -> None:
        """
        Инициализация страницы корзины.
        
        :param driver: WebDriver instance
        """
        self.driver = driver
    
    def get_items_count(self) -> int:
        """
        Получение количества товаров в корзине.
        
        :return: Количество товаров
        """
        cart_items = self.driver.find_elements(By.CLASS_NAME, "cart_item")
        return len(cart_items)
    
    def click_checkout(self) -> None:
        """Нажатие кнопки оформления заказа."""
        self.driver.find_element(By.ID, "checkout").click()