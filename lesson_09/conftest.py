import pytest
import sqlite3
import os


@pytest.fixture(scope='function')
def db_connection():
    """Создание подключения к SQLite для каждого теста."""
    if os.path.exists('test.db'):
        os.remove('test.db')
    
    conn = sqlite3.connect('test.db')
    cursor = conn.cursor()
    
    cursor.execute('''
    CREATE TABLE students (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        age INTEGER NOT NULL,
        is_active BOOLEAN DEFAULT TRUE
    )
    ''')
    
    yield conn
    
    conn.close()
    if os.path.exists('test.db'):
        os.remove('test.db')