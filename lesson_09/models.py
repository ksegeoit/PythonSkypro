from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Student(Base):
    """Модель студента с поддержкой soft delete"""
    __tablename__ = 'students'
    
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    age = Column(Integer, nullable=False)
    is_active = Column(Boolean, default=True)
    
    def soft_delete(self):
        """Мягкое удаление записи"""
        self.is_active = False