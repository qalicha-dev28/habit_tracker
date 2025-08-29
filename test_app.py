#!/usr/bin/env python3
"""
Test the basic functionality of the habit tracker
"""
from models import session, Category, Habit
from crud import create_category, create_habit, get_all_categories, get_all_habits

# Test database connection
print("Testing database connection...")
categories = get_all_categories()
print(f"Found {len(categories)} categories")

habits = get_all_habits()
print(f"Found {len(habits)} habits")

print("✅ Basic functionality test passed!")
