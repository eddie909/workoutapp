from config import db


class Routine(db.Model):
    id=db.Column(db.Integer, primary_key=True)
    name=db.Column(db.String(80), unique=True, nullable=False)
    user_id=db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    workouts=db.relationship('UserWorkout',backref='routine',lazy=True)
    
    def __init__(self,name,user_id):
        self.name=name
        self.user_id=user_id

    def __repr__(self):
        return f'Routine: {self.name}'
    
    