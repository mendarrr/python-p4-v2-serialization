from random import choice as rc
from faker import Faker

from app import app
from models import db, Pet

with app.app_context():

    # Create and initialize a faker generator
    fake = Faker()

    # Delete all rows in the "pets" table
    Pet.query.delete()

    # Create an empty list
    pets = []

    species = ['Dog', 'Cat', 'Chicken', 'Hamster', 'Turtle']

    # Add some Pet instances to the list
    for n in range(10):
        pet = Pet(name=fake.first_name(), species=rc(species))
        pets.append(pet)

    # Insert each Pet in the list into the "pets" table
    db.session.add_all(pets)

    # Commit the transaction
    db.session.commit()