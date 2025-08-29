from models import Base, engine

def setup_database():
    Base.metadata.create_all(engine)
    print("✅ Database setup complete! Your habit tracker is ready.")

if __name__ == "__main__":
    setup_database()