from models import session, Category, Habit, Completion
from crud import get_all_categories, get_all_habits, get_completions
from datetime import date, timedelta

def debug_info():
    print("🐛 Debug Information")
    print("=" * 50)
    
    categories = get_all_categories()
    print(f"📂 Categories: {len(categories)}")
    for cat in categories:
        print(f"   {cat.id}: {cat.name}")
    
    habits = get_all_habits()
    print(f"\n🌿 Habits: {len(habits)}")
    for habit in habits:
        completions = get_completions(habit.id)
        print(f"   {habit.id}: {habit.name} (Streak: {habit.streak}, Completions: {len(completions)})")
    
    print(f"\n💾 Database: habit_tracker.db")
    print("✅ Debug check complete!")

def test_operations():
    print("\n🧪 Testing Operations")
    print("=" * 50)
    
    try:
        categories = get_all_categories()
        print("✅ Categories query: OK")
        
        habits = get_all_habits()
        print("✅ Habits query: OK")
        
        if habits:
            streak = habits[0].streak
            print("✅ Streak access: OK")
        
        print("✅ All tests passed!")
        
    except Exception as e:
        print(f"❌ Error: {e}")

if __name__ == "__main__":
    debug_info()
    test_operations()