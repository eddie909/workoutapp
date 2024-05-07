from sqlalchemy import JSON
from config import db

class Workout(db.Model):
    id=db.Column(db.Integer,unique=True, primary_key=True)
    bodypart=db.Column(db.String(20),unique=False, nullable=False)
    equipment=db.Column(db.String(80), unique=False, nullable=False)
    gif=db.Column(db.String(120), unique=False, nullable=False)
    name=db.Column(db.String(120), unique=False, nullable=False)
    target=db.Column(db.String(120), unique=False, nullable=False)
    secondaryMuscles=db.Column(JSON, unique=False, nullable=False)
    instructions=db.Column(JSON, unique=False, nullable=False)

    def __init__(self,bodypart,equipment,gif,name,target,secondaryMuscles,instructions):
        self.bodypart=bodypart
        self.equipment=equipment
        self.gif=gif
        self.name=name
        self.target=target
        self.secondaryMuscles=secondaryMuscles
        self.instructions=instructions
        

    def __repr__(self):
        return f'<Workout: {self.name}>'
    
    def to_json(self):
        return {
            "id": self.id,
            "equipment": self.equipment,
            "gif": self.gif,
            "name": self.name,
            "target": self.target,
            "secondaryMuscles": self.secondaryMuscles,
            "instructions": self.instructions
        }