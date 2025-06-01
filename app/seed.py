# app/seed.py

from models import Game, session
from faker import Faker
import random

# Initialize Faker
fake = Faker()

# Clear old data
session.query(Game).delete()
session.commit()

# Add console message
print("Seeding games...")

# Generate 50 random games
games = [
    Game(
        title=fake.name(),
        genre=fake.word(),
        platform=fake.word(),
        price=random.randint(0, 60)
    )
    for i in range(50)
]

# Save to the database
session.bulk_save_objects(games)
session.commit()
print("Seeding complete.")

