from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver


class OrderPage:
    """Класс для работы со страницей оформления заказа."""
    
    def __init__(self, driver: WebDriver) -> None:
        """
        Инициализация страницы оформления заказа.
        
        :param driver: WebDriver instance
        """
        self.driver = driver
    
    def fill_info(self, first_name: str, last_name: str, zip_code: str) -> None:
        """
        Заполнение информации для оформления заказа.
        
        :param first_name: Имя
        :param last_name: Фамилия
        :param zip_code: Почтовый индекс
        """
        self.driver.find_element(By.ID, "first-name").send_keys(first_name)
        self.driver.find_element(By.ID, "last-name").send_keys(last_name)
        self.driver.find_element(By.ID, "postal-code").send_keys(zip_code)
        self.driver.find_element(By.ID, "continue").click()
    
    def finish_order(self) -> None:
        """Завершение оформления заказа."""
        self.driver.find_element(By.ID, "finish").click()
    
    def is_order_complete(self) -> bool:
        """
        Проверка успешного оформления заказа.
        
        :return: True если заказ оформлен успешно, иначе False
        """
        return "Thank you for your order" in self.driver.page_source