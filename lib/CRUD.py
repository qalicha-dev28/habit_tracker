from models import session, Category, Habit, Completion
from datetime import date, datetime, timedelta
from sqlalchemy import desc

def create_category(name):
    category = Category(name=name)
    session.add(category)
    session.commit()
    return category

def get_all_categories():
    return session.query(Category).all()

def get_category_by_id(category_id):
    return session.query(Category).filter(Category.id == category_id).first()

def create_habit(name, description, category_id):
    habit = Habit(name=name, description=description, category_id=category_id)
    session.add(habit)
    session.commit()
    return habit

def get_all_habits():
    return session.query(Habit).all()

def get_habits_by_category(category_id):
    return session.query(Habit).filter(Habit.category_id == category_id).all()

def get_habit_by_id(habit_id):
    return session.query(Habit).filter(Habit.id == habit_id).first()

def log_completion(habit_id, notes=None):
    today = date.today()
    existing_completion = session.query(Completion).filter(
        Completion.habit_id == habit_id,
        Completion.date == today
    ).first()
    
    if existing_completion:
        return None
    
    completion = Completion(habit_id=habit_id, date=today, notes=notes)
    session.add(completion)
    
    habit = get_habit_by_id(habit_id)
    yesterday = today - timedelta(days=1)
    
    yesterday_completion = session.query(Completion).filter(
        Completion.habit_id == habit_id,
        Completion.date == yesterday
    ).first()
    
    if yesterday_completion:
        habit.streak += 1
    else:
        habit.streak = 1
    
    session.commit()
    return completion

def get_completions(habit_id):
    return session.query(Completion).filter(
        Completion.habit_id == habit_id
    ).order_by(desc(Completion.date)).all()

def get_habit_streak(habit_id):
    habit = get_habit_by_id(habit_id)
    return habit.streak if habit else 0

def get_today_completions():
    today = date.today()
    return session.query(Completion).filter(Completion.date == today).all()

def get_longest_streak():
    habits = session.query(Habit).order_by(desc(Habit.streak)).all()
    return habits[0] if habits else None