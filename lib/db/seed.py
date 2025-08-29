from models import session, Category, Habit
from crud import create_category, create_habit

def seed_data():
    # Create categories
    health = create_category("Health & Wellness")
    productivity = create_category("Productivity")
    learning = create_category("Learning")
    
    # Create habits
    create_habit("Drink water", "Drink 8 glasses of water daily", health.id)
    create_habit("Exercise", "30 minutes of physical activity", health.id)
    create_habit("Meditate", "10 minutes of meditation", health.id)
    create_habit("Read", "Read for 30 minutes", learning.id)
    create_habit("Plan day", "Plan the day's tasks", productivity.id)
    
    print("Sample data added successfully!")

if __name__ == "__main__":
    seed_data()