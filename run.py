from flask import Flask
from config import db, app
from controllers.workouts import cacheWorkouts
from views import views
from models.workouts import Workout
from models.routines import Routine
from models.userworkouts import UserWorkout
from models.user import User



def create_app():
    # db.drop_all()
    # Routine.__table__.drop(db.engine)
    # UserWorkout.__table__.drop(db.engine)
    # User.__table__.drop(db.engine)
    db.create_all()
    return app

def load_views():
    for view in views:
        app.register_blueprint(view)

def is_database_populated():
    return db.session.query(Workout).count() > 0

def populateDatabase():
    if not is_database_populated():
        cacheWorkouts()
     

def init_app():
    create_app()
    load_views()
    populateDatabase()



with app.app_context():
   init_app()






