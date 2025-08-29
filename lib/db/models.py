from sqlalchemy import create_engine, Column, Integer, String, Text, Date, DateTime, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship
from datetime import datetime
import os

Base = declarative_base()

class Category(Base):
    __tablename__ = 'categories'
    
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    created_at = Column(DateTime, default=datetime.now)
    
    habits = relationship('Habit', back_populates='category')
    
    def __repr__(self):
        return f"<Category '{self.name}'>"

class Habit(Base):
    __tablename__ = 'habits'
    
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    description = Column(Text)
    streak = Column(Integer, default=0)
    created_at = Column(DateTime, default=datetime.now)
    category_id = Column(Integer, ForeignKey('categories.id'))
    
    category = relationship('Category', back_populates='habits')
    completions = relationship('Completion', back_populates='habit')
    
    def __repr__(self):
        return f"<Habit '{self.name}' (Streak: {self.streak} days)>"

class Completion(Base):
    __tablename__ = 'completions'
    
    id = Column(Integer, primary_key=True)
    date = Column(Date, nullable=False)
    notes = Column(Text)
    created_at = Column(DateTime, default=datetime.now)
    habit_id = Column(Integer, ForeignKey('habits.id'))
    
    habit = relationship('Habit', back_populates='completions')
    
    def __repr__(self):
        return f"<Completion for habit {self.habit_id} on {self.date}>"

DATABASE_URL = 'sqlite:///habit_tracker.db'
engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)
session = Session()

Base.metadata.create_all(engine)