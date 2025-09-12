import requests
import os


class YougileAPIClient:
    BASE_URL = "https://ru.yougile.com/api-v2"
    
    def __init__(self, token=None):
        self.token = token or os.getenv(
            "YOUGILE_TOKEN", 
            "P043ZyEQiSJbr-N7GXqOKvsgBr4izHsLA6D9ZtLa4vJFlylj2NFYW6NFPq8BM6OK"
        )
        self.headers = {
            "Authorization": f"Bearer {self.token}",
            "Content-Type": "application/json"
        }
    
    def create_project(self, data):
        response = requests.post(
            f"{self.BASE_URL}/projects",
            json=data,
            headers=self.headers
        )
        return response
    
    def get_project(self, project_id):
        response = requests.get(
            f"{self.BASE_URL}/projects/{project_id}",
            headers=self.headers
        )
        return response
    
    def update_project(self, project_id, data):
        response = requests.put(
            f"{self.BASE_URL}/projects/{project_id}",
            json=data,
            headers=self.headers
        )
        return response
    
    def delete_project(self, project_id):
        response = requests.delete(
            f"{self.BASE_URL}/projects/{project_id}",
            headers=self.headers
        )
        return response