def test_add_student(db_connection):
    """Тест добавления студента."""
    cursor = db_connection.cursor()
    
    cursor.execute(
        "INSERT INTO students (name, age) VALUES (?, ?)", 
        ("Иван Иванов", 20)
    )
    db_connection.commit()
    
    cursor.execute(
        "SELECT * FROM students WHERE name = ?", 
        ("Иван Иванов",)
    )
    result = cursor.fetchone()
    
    assert result is not None
    assert result[2] == 20
    assert result[3] == 1


def test_update_student(db_connection):
    """Тест изменения данных студента."""
    cursor = db_connection.cursor()
    
    cursor.execute(
        "INSERT INTO students (name, age) VALUES (?, ?)", 
        ("Мария Петрова", 22)
    )
    db_connection.commit()
    
    cursor.execute(
        "UPDATE students SET age = ? WHERE name = ?", 
        (23, "Мария Петрова")
    )
    db_connection.commit()
    
    cursor.execute(
        "SELECT age FROM students WHERE name = ?", 
        ("Мария Петрова",)
    )
    result = cursor.fetchone()
    
    assert result[0] == 23


def test_soft_delete_student(db_connection):
    """Тест мягкого удаления студента."""
    cursor = db_connection.cursor()
    
    cursor.execute(
        "INSERT INTO students (name, age) VALUES (?, ?)", 
        ("Тест Тестов", 25)
    )
    db_connection.commit()
    
    cursor.execute(
        "UPDATE students SET is_active = FALSE WHERE name = ?", 
        ("Тест Тестов",)
    )
    db_connection.commit()
    
    cursor.execute(
        "SELECT is_active FROM students WHERE name = ?", 
        ("Тест Тестов",)
    )
    result = cursor.fetchone()
    
    assert result is not None
    assert result[0] == 0