import click
from crud import (
    create_category, get_all_categories,
    create_habit, get_all_habits, get_habits_by_category,
    log_completion, get_completions, get_habit_streak
)
from models import session
from datetime import date

@click.group()
def cli():
    """Habit Tracker CLI - Track your daily habits and build streaks"""
    pass

@cli.command()
@click.option('--name', prompt='Category name', help='Name of the category')
def add_category(name):
    """Add a new category"""
    category = create_category(name)
    click.echo(f"Category '{category.name}' added with ID: {category.id}")

@cli.command()
def list_categories():
    """List all categories"""
    categories = get_all_categories()
    if not categories:
        click.echo("No categories found.")
        return
    
    click.echo("Categories:")
    for category in categories:
        click.echo(f"  {category.id}: {category.name}")

@cli.command()
@click.option('--name', prompt='Habit name', help='Name of the habit')
@click.option('--description', prompt='Habit description', help='Description of the habit')
@click.option('--category-id', prompt='Category ID', type=int, help='ID of the category')
def add_habit(name, description, category_id):
    """Add a new habit"""
    habit = create_habit(name, description, category_id)
    click.echo(f"Habit '{habit.name}' added with ID: {habit.id}")

@cli.command()
def list_habits():
    """List all habits"""
    habits = get_all_habits()
    if not habits:
        click.echo("No habits found.")
        return
    
    click.echo("Habits:")
    for habit in habits:
        click.echo(f"  {habit.id}: {habit.name} (Streak: {habit.streak} days)")

@cli.command()
@click.option('--habit-id', prompt='Habit ID', type=int, help='ID of the habit to complete')
@click.option('--notes', prompt='Notes (optional)', default='', help='Notes about this completion')
def complete_habit(habit_id, notes):
    """Log completion of a habit for today"""
    completion = log_completion(habit_id, notes or None)
    if completion:
        click.echo(f"Completed habit {completion.habit.name} on {completion.date}")
        click.echo(f"Current streak: {completion.habit.streak} days")
    else:
        click.echo("This habit was already completed today.")

@cli.command()
@click.option('--habit-id', prompt='Habit ID', type=int, help='ID of the habit to check')
def check_streak(habit_id):
    """Check the current streak for a habit"""
    streak = get_habit_streak(habit_id)
    habit = session.query(Habit).filter(Habit.id == habit_id).first()
    if habit:
        click.echo(f"Current streak for '{habit.name}': {streak} days")
    else:
        click.echo("Habit not found.")

@cli.command()
@click.option('--habit-id', prompt='Habit ID', type=int, help='ID of the habit to view history')
def view_history(habit_id):
    """View completion history for a habit"""
    completions = get_completions(habit_id)
    habit = session.query(Habit).filter(Habit.id == habit_id).first()
    
    if not habit:
        click.echo("Habit not found.")
        return
        
    if not completions:
        click.echo(f"No completions found for '{habit.name}'.")
        return
    
    click.echo(f"Completion history for '{habit.name}':")
    for completion in completions:
        notes = f" - {completion.notes}" if completion.notes else ""
        click.echo(f"  {completion.date}{notes}")

if __name__ == '__main__':
    cli()