from .db import Base, engine, Session, Category, Habit, Completion
from .db.seed import seed_database

def debug_database():
    # Reset database
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)
    
    # Seed with sample data
    seed_database()
    
    # Test queries
    session = Session()
    
    print("\n=== Categories ===")
    categories = session.query(Category).all()
    for cat in categories:
        print(f"{cat.id}: {cat.name}")
    
    print("\n=== Habits ===")
    habits = session.query(Habit).all()
    for habit in habits:
        print(f"{habit.id}: {habit.name} (Streak: {habit.streak})")
    
    print("\n=== Completions ===")
    completions = session.query(Completion).limit(5).all()
    for comp in completions:
        print(f"Habit {comp.habit_id}: {comp.date}")
    
    session.close()
    print("\n✅ Debug completed successfully!")

if __name__ == '__main__':
    debug_database()