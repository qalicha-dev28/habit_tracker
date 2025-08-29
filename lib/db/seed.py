from models import session
from crud import create_category, create_habit
from datetime import datetime, timedelta

def seed_data():
    print("🌱 Seeding sample data...")
    
    health = create_category("Health & Wellness")
    productivity = create_category("Productivity")
    learning = create_category("Learning & Growth")
    mindfulness = create_category("Mindfulness")
    
    water = create_habit("Drink Water", "Drink 8 glasses of water daily", health.id)
    exercise = create_habit("Morning Exercise", "30 minutes of physical activity", health.id)
    meditation = create_habit("Daily Meditation", "10 minutes of mindfulness practice", mindfulness.id)
    reading = create_habit("Read Books", "Read for 30 minutes daily", learning.id)
    planning = create_habit("Plan Day", "Plan the day's tasks each morning", productivity.id)
    gratitude = create_habit("Gratitude Journal", "Write 3 things I'm grateful for", mindfulness.id)
    
    print("✅ Sample data added successfully!")
    print("\n📋 Your sample habits:")
    print(f"   💧 {water.name} (Health)")
    print(f"   🏃‍♀️ {exercise.name} (Health)")
    print(f"   🧘‍♀️ {meditation.name} (Mindfulness)")
    print(f"   📚 {reading.name} (Learning)")
    print(f"   📅 {planning.name} (Productivity)")
    print(f"   🙏 {gratitude.name} (Mindfulness)")
    print("\n🚀 Start tracking with: python cli.py list-habits")

if __name__ == "__main__":
    seed_data()