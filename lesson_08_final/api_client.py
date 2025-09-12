import requests
import os


class YougileAPIClient:
    """Клиент для работы с API Yougile."""
    
    BASE_URL = "https://ru.yougile.com/api-v2"
    
    def __init__(self, token=None):
        """Инициализация клиента API.
        
        Args:
            token (str, optional): Токен авторизации.
        """
        self.token = token or os.getenv(
            "YOUGILE_TOKEN",
            "P043ZyEQiSJbr-N7GXqOKvsgBr4izHsLA6D9ZtLa4vJFlylj2NFYW6NFPq8BM6OK"
        )
        self.headers = {
            "Authorization": f"Bearer {self.token}",
            "Content-Type": "application/json"
        }
    
    def create_project(self, data):
        """Создает новый проект.
        
        Args:
            data (dict): Данные для создания проекта
            
        Returns:
            Response: Ответ от API
        """
        response = requests.post(
            f"{self.BASE_URL}/projects",
            json=data,
            headers=self.headers
        )
        return response
    
    def get_project(self, project_id):
        """Получает информацию о проекте.
        
        Args:
            project_id (str): ID проекта
            
        Returns:
            Response: Ответ от API
        """
        response = requests.get(
            f"{self.BASE_URL}/projects/{project_id}",
            headers=self.headers
        )
        return response
    
    def update_project(self, project_id, data):
        """Обновляет информацию о проекте.
        
        Args:
            project_id (str): ID проекта
            data (dict): Данные для обновления
            
        Returns:
            Response: Ответ от API
        """
        response = requests.put(
            f"{self.BASE_URL}/projects/{project_id}",
            json=data,
            headers=self.headers
        )
        return response
    
    def delete_project(self, project_id):
        """Удаляет проект.
        
        Args:
            project_id (str): ID проекта
            
        Returns:
            Response: Ответ от API
        """
        response = requests.delete(
            f"{self.BASE_URL}/projects/{project_id}",
            headers=self.headers
        )
        return response
