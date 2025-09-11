from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver


class AuthPage:
    """Класс для работы со страницей авторизации."""
    
    def __init__(self, driver: WebDriver) -> None:
        """
        Инициализация страницы авторизации.
        
        :param driver: WebDriver instance
        """
        self.driver = driver
        self.url = "https://www.saucedemo.com/"
    
    def open(self) -> None:
        """Открыть страницу авторизации."""
        self.driver.get(self.url)
    
    def enter_username(self, username: str) -> None:
        """
        Ввод имени пользователя.
        
        :param username: Логин пользователя
        """
        self.driver.find_element(By.ID, "user-name").send_keys(username)
    
    def enter_password(self, password: str) -> None:
        """
        Ввод пароля.
        
        :param password: Пароль пользователя
        """
        self.driver.find_element(By.ID, "password").send_keys(password)
    
    def click_login(self) -> None:
        """Нажатие кнопки входа."""
        self.driver.find_element(By.ID, "login-button").click()
    
    def auth(self, username: str, password: str) -> None:
        """
        Полная авторизация пользователя.
        
        :param username: Логин пользователя
        :param password: Пароль пользователя
        """
        self.enter_username(username)
        self.enter_password(password)
        self.click_login()