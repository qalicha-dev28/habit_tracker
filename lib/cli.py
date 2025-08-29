import click
from crud import (
    create_category, get_all_categories, get_category_by_id,
    create_habit, get_all_habits, get_habits_by_category,
    log_completion, get_completions, get_habit_streak,
    get_today_completions, get_longest_streak
)
from models import session
from datetime import date

@click.group()
def cli():
    """Najma's Habit Tracker - Build better habits every day"""
    pass

@cli.command()
@click.option('--name', prompt='✨ Category name', help='Name of the category')
def add_category(name):
    category = create_category(name)
    click.echo(f"✅ Category '{category.name}' added (ID: {category.id})")

@cli.command()
def list_categories():
    categories = get_all_categories()
    if not categories:
        click.echo("📭 No categories found. Create one with 'add-category'")
        return
    
    click.echo("📋 Your Categories:")
    for category in categories:
        click.echo(f"   {category.id}: {category.name}")

@cli.command()
@click.option('--name', prompt='🌱 Habit name', help='Name of the habit')
@click.option('--description', prompt='📝 Habit description', help='Description of the habit')
@click.option('--category-id', prompt='🏷️  Category ID', type=int, help='ID of the category')
def add_habit(name, description, category_id):
    habit = create_habit(name, description, category_id)
    click.echo(f"✅ Habit '{habit.name}' added (ID: {habit.id})")

@cli.command()
def list_habits():
    habits = get_all_habits()
    if not habits:
        click.echo("📭 No habits found. Create one with 'add-habit'")
        return
    
    click.echo("🌿 Your Habits:")
    for habit in habits:
        category = get_category_by_id(habit.category_id)
        click.echo(f"   {habit.id}: {habit.name} (Streak: {habit.streak} days, Category: {category.name})")

@cli.command()
@click.option('--habit-id', prompt='🎯 Habit ID', type=int, help='ID of the habit to complete')
@click.option('--notes', prompt='💭 Notes (optional)', default='', help='Notes about this completion')
def complete_habit(habit_id, notes):
    completion = log_completion(habit_id, notes or None)
    if completion:
        click.echo(f"🎉 Completed '{completion.habit.name}' on {completion.date}!")
        click.echo(f"🔥 Current streak: {completion.habit.streak} days")
    else:
        click.echo("⚠️  This habit was already completed today.")

@cli.command()
@click.option('--habit-id', prompt='📊 Habit ID', type=int, help='ID of the habit to check')
def check_streak(habit_id):
    streak = get_habit_streak(habit_id)
    habit = session.query(Habit).filter(Habit.id == habit_id).first()
    if habit:
        click.echo(f"📈 Current streak for '{habit.name}': {streak} days")
    else:
        click.echo("❌ Habit not found.")

@cli.command()
@click.option('--habit-id', prompt='📅 Habit ID', type=int, help='ID of the habit to view history')
def view_history(habit_id):
    completions = get_completions(habit_id)
    habit = session.query(Habit).filter(Habit.id == habit_id).first()
    
    if not habit:
        click.echo("❌ Habit not found.")
        return
        
    if not completions:
        click.echo(f"📭 No completions found for '{habit.name}'.")
        return
    
    click.echo(f"📅 Completion history for '{habit.name}':")
    for completion in completions:
        notes = f" - {completion.notes}" if completion.notes else ""
        click.echo(f"   📌 {completion.date}{notes}")

@cli.command()
def today():
    completions = get_today_completions()
    if not completions:
        click.echo("📭 No habits completed today yet.")
        return
    
    click.echo("✅ Today's completed habits:")
    for completion in completions:
        click.echo(f"   🌟 {completion.habit.name}")

@cli.command()
def stats():
    habits = get_all_habits()
    longest_streak = get_longest_streak()
    
    click.echo("📊 Your Habit Statistics:")
    click.echo(f"   📈 Total habits: {len(habits)}")
    
    if longest_streak:
        click.echo(f"   🏆 Longest streak: {longest_streak.streak} days ({longest_streak.name})")
    else:
        click.echo("   🏆 No streaks yet - start building habits!")

@cli.command()
def reset_db():
    from models import Base, engine
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)
    click.echo("🔄 Database reset complete!")

if __name__ == '__main__':
    cli()