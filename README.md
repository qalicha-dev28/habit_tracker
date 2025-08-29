Habit Tracker

A command-line interface application designed to help users efficiently track and manage their daily habits. This tool provides an organized way to monitor habit completion, track streaks, and maintain consistency in personal routines.
Key Features

    Habit Management: Create and categorize personal habits with detailed descriptions

    Completion Tracking: Log daily completions of habits with optional notes

    Streak Monitoring: Automatically track consecutive days of habit completion

    Progress History: View completion history for each habit over time

    Statistics Overview: Access habit statistics and performance metrics

    Category Organization: Group habits into categories for better organization

Technical Stack

This application is built with a modern Python development stack, focusing on reliability, maintainability, and user experience.

Core Technologies:

    Python 3.8+: The programming language used for application development

    SQLAlchemy: SQL toolkit and Object-Relational Mapping (ORM) library for database operations

    Click: Python package for creating beautiful command-line interfaces

    SQLite: Lightweight disk-based database that doesn't require a separate server process

Development Tools:

    Pipenv: Python dependency management and virtual environment tool

    Alembic (Optional): Lightweight database migration tool for SQLAlchemy

Project Architecture

The project follows a modular structure with clear separation of concerns:
text

/habit_tracker
├── models.py          # Database models and schema definitions
├── crud.py            # Database operations and CRUD functions
├── cli.py             # Main command-line interface
├── main.py            # Alternative entry point for the application
├── setup.py           # Database initialization script
├── seed.py            # Sample data population
├── debug.py           # Debugging and diagnostic utilities
├── __init__.py        # Package initialization
├── Pipfile            # Dependency management configuration
├── Pipfile.lock       # Locked dependency versions
└── README.md          # Project documentation

Local Development Setup

To run the Habit Tracker on your local machine for development, follow these instructions.
Prerequisites

Ensure you have the following software installed on your system:

    Python 3.8 or higher: Programming language runtime

    Pipenv: Python dependency management tool (install via pip install pipenv)

Step 1: Clone the Repository

Begin by cloning the project repository from GitHub to your local machine:
bash

git clone <repository-url>
cd habit_tracker

Step 2: Set Up Virtual Environment and Dependencies

Install project dependencies using Pipenv:
bash

pipenv install

Activate the virtual environment:
bash

pipenv shell

Step 3: Initialize the Database

Set up the database schema:
bash

python setup.py

Step 4: Add Sample Data (Optional)

Populate the database with sample habits and categories:
bash

python seed.py

Step 5: Run the Application

Start using the habit tracker:
bash

python cli.py --help

Usage
Basic Commands

View available commands:
bash

python cli.py --help

List all habits:
bash

python cli.py list-habits

Add a new habit:
bash

python cli.py add-habit

Complete a habit for today:
bash

python cli.py complete-habit --habit-id 1

Check habit streak:
bash

python cli.py check-streak --habit-id 1

View habit history:
bash

python cli.py view-history --habit-id 1

Advanced Usage

View statistics:
bash

python cli.py stats

See today's completions:
bash

python cli.py today

Reset database (warning: deletes all data):
bash

python cli.py reset-db

Database Schema

The application uses a SQLite database with three main tables:

    categories - Stores habit categories

        id (Integer, Primary Key)

        name (String)

        created_at (DateTime)

    habits - Stores individual habits

        id (Integer, Primary Key)

        name (String)

        description (Text)

        streak (Integer)

        created_at (DateTime)

        category_id (Integer, Foreign Key to categories)

    completions - Stores daily habit completions

        id (Integer, Primary Key)

        date (Date)

        notes (Text)

        created_at (DateTime)

        habit_id (Integer, Foreign Key to habits)

Deployment

The Habit Tracker is designed to run locally and doesn't require external deployment. The SQLite database file (habit_tracker.db) is created automatically in your project directory.
Environment Configuration

For production use, you can configure the database connection by setting the DATABASE_URL environment variable in a .env file:
ini

DATABASE_URL=sqlite:///habit_tracker.db

Contributing

Contributions are welcome! If you have suggestions for improvements, new features, or encounter any issues, please feel free to fork this repository, open an issue, or submit a pull request.
License

This project is open-source and distributed under the MIT License.
