# Тестирование интернет-магазина

## Описание проекта
Автоматизированное тестирование интернет-магазина с использованием Selenium, pytest и Allure.

## Запуск тестов
1. Установите зависимости: `pip install -r requirements.txt`
2. Запустите тесты: `pytest --alluredir=allure_results lesson_10/ -v`
3. Сгенерируйте отчет: `allure serve allure_results`

## Требования
- Python 3.8+
- Chrome browser
- ChromeDriver