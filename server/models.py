# server/models.py

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Pet(db.Model,):
    __tablename__ = 'pets'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    species = db.Column(db.String)
    breed = db.Column(db.String)
    age = db.Column(db.Integer)  # Add this line for 'age'

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'species': self.species,
            'breed': self.breed,
            'age': self.age,  # Add this to include 'age' in the response
        }
