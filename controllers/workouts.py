from models import Workout
from config import db
from apidata import fetchdata
import json

def cacheWorkouts():
    bodyparts=['back','cardio','chest','lower arms','lower legs','neck','shoulders','upper arms','upper legs','waist']

    for body in bodyparts:
        data=fetchdata(body,10)
        data=json.loads(data)
        for workout in data:
            addWorkout(workout['bodyPart'],workout['equipment'],workout['gifUrl'],workout['name'],workout['target'],workout['secondaryMuscles'],workout['instructions'])
            
    return None

def addWorkout(bodypart,equipment, gif, name, target,secondaryMuscles,instructions):
    w = Workout.query.filter_by(bodypart=bodypart,equipment=equipment, gif=gif, name=name, target=target,secondaryMuscles=secondaryMuscles,instructions=instructions).first()
    # sm=json.dumps(secondaryMuscles)
    # ins=json.dumps(instructions)
    if not w :
        new_workout=Workout(bodypart=bodypart,equipment=equipment,gif=gif,name=name,target=target,secondaryMuscles=secondaryMuscles,instructions=instructions)
        db.session.add(new_workout)
        db.session.commit()
        return w
    else:
        return None
        
    
def getWorkoutbyName(name):
    return Workout.query.filter_by(name=name).first()

def getAllWorkouts():
    return Workout.query.all()

def getWorkoutbyBody(body):
    return Workout.query.filter_by(bodypart=body).all()