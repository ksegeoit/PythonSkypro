import time
from api_client import YougileAPIClient


class TestProjectsPositive:
    """Позитивные тесты для методов работы с проектами."""
    
    def test_create_project(self, api_client):
        """Тест создания проекта с валидными данными."""
        data = {
            "title": f"New Test Project {time.time()}"
        }
        response = api_client.create_project(data)
        
        assert response.status_code == 201
        assert "id" in response.json()
        
        project_id = response.json()["id"]
        get_response = api_client.get_project(project_id)
        
        assert get_response.status_code == 200
        assert get_response.json()["title"] == data["title"]
        
        api_client.delete_project(project_id)

    def test_get_project(self, api_client, created_project):
        """Тест получения информации о проекте."""
        response = api_client.get_project(created_project)
        
        assert response.status_code == 200
        assert response.json()["id"] == created_project
        assert "title" in response.json()

    def test_update_project(self, api_client, created_project):
        """Тест обновления информации о проекте."""
        get_response = api_client.get_project(created_project)
        assert get_response.status_code == 200
        original_title = get_response.json()["title"]
        
        new_title = f"Updated Test Project {time.time()}"
        update_data = {"title": new_title}
        response = api_client.update_project(created_project, update_data)
        
        assert response.status_code == 200
        
        get_response_after_update = api_client.get_project(created_project)
        
        assert get_response_after_update.status_code == 200
        assert get_response_after_update.json()["title"] == new_title
        assert get_response_after_update.json()["title"] != original_title


class TestProjectsNegative:
    """Негативные тесты для методов работы с проектами."""
    
    def test_create_project_without_title(self, api_client):
        """Тест создания проекта без названия."""
        data = {}
        response = api_client.create_project(data)
        
        assert response.status_code == 400

    def test_get_nonexistent_project(self, api_client):
        """Тест получения несуществующего проекта."""
        response = api_client.get_project("nonexistent-project-id-12345")
        
        assert response.status_code == 404

    def test_update_nonexistent_project(self, api_client):
        """Тест обновления несуществующего проекта."""
        update_data = {"title": "Updated Title"}
        nonexistent_id = "nonexistent-project-id-12345"
        response = api_client.update_project(nonexistent_id, update_data)
        
        assert response.status_code == 404

    def test_create_project_with_invalid_token(self):
        """Тест создания проекта с неверным токеном."""
        invalid_client = YougileAPIClient("invalid_token")
        
        data = {"title": "Test Project"}
        response = invalid_client.create_project(data)
        
        assert response.status_code == 401
        
    def test_create_project_with_empty_title(self, api_client):
        """Тест создания проекта с пустым названием."""
        data = {"title": ""}
        response = api_client.create_project(data)
        
        assert response.status_code == 400
        
    def test_update_project_with_empty_title(self, api_client, created_project):
        """Тест обновления проекта с пустым названием."""
        update_data = {"title": ""}
        response = api_client.update_project(created_project, update_data)
        
        assert response.status_code == 400