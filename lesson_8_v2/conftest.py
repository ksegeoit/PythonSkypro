import pytest
import time
from api_client import YougileAPIClient


@pytest.fixture(scope="session")
def api_client():
    """Фикстура для создания клиента API."""
    return YougileAPIClient()


@pytest.fixture
def test_project(api_client):
    """Фикстура для создания тестового проекта.
    
    Создает проект перед тестом и удаляет его после завершения.
    """
    project_data = {
        "title": f"Test Project {time.time()}",
    }
    response = api_client.create_project(project_data)
    
    if response.status_code != 201:
        error_msg = f"Не удалось создать тестовый проект: {response.status_code}"
        pytest.skip(error_msg)
    
    project_id = response.json()["id"]
    
    yield project_id
    
    api_client.delete_project(project_id)