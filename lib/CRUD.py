from models import session, Category, Habit, Completion
from datetime import date, datetime, timedelta
from sqlalchemy import desc

def create_category(name):
    """Create a new category"""
    category = Category(name=name)
    session.add(category)
    session.commit()
    return category

def get_all_categories():
    """Get all categories"""
    return session.query(Category).all()

def create_habit(name, description, category_id):
    """Create a new habit"""
    habit = Habit(
        name=name, 
        description=description, 
        category_id=category_id
    )
    session.add(habit)
    session.commit()
    return habit

def get_all_habits():
    """Get all habits"""
    return session.query(Habit).all()

def get_habits_by_category(category_id):
    """Get habits by category"""
    return session.query(Habit).filter(Habit.category_id == category_id).all()

def get_habit_by_id(habit_id):
    """Get a habit by ID"""
    return session.query(Habit).filter(Habit.id == habit_id).first()

def log_completion(habit_id, notes=None):
    """Log a completion for a habit"""
    # Check if already completed today
    today = date.today()
    existing_completion = session.query(Completion).filter(
        Completion.habit_id == habit_id,
        Completion.date == today
    ).first()
    
    if existing_completion:
        return None  # Already completed today
    
    completion = Completion(
        habit_id=habit_id,
        date=today,
        notes=notes
    )
    
    session.add(completion)
    
    # Update streak
    habit = get_habit_by_id(habit_id)
    yesterday = today - timedelta(days=1)
    
    # Check if there was a completion yesterday
    yesterday_completion = session.query(Completion).filter(
        Completion.habit_id == habit_id,
        Completion.date == yesterday
    ).first()
    
    if yesterday_completion:
        habit.streak += 1
    else:
        # If no completion yesterday, reset streak to 1
        habit.streak = 1
    
    session.commit()
    return completion

def get_completions(habit_id):
    """Get all completions for a habit"""
    return session.query(Completion).filter(
        Completion.habit_id == habit_id
    ).order_by(desc(Completion.date)).all()

def get_habit_streak(habit_id):
    """Get the current streak for a habit"""
    habit = get_habit_by_id(habit_id)
    return habit.streak if habit else 0