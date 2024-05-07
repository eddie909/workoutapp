from config import db
from models import (Workout , UserWorkout)

def getUserWorkoutbyName(name):
    return UserWorkout.query.filter_by(name=name).first()

def getWorkoutbyBody(body):
    return UserWorkout.query.filter_by(bodypart=body).all()

def addUserWorkout(workout_id,routine_id,day,user_id):
    u=UserWorkout.query.filter_by(workout_id=workout_id,routine_id=routine_id,user_id=user_id).first()

    if not u:
        u=UserWorkout(workout_id=workout_id,routine_id=routine_id,day=day,user_id=user_id)
        db.session.add(u)
        db.session.commit()
        return u
    else:
        return None

def deleteUserWorkout(workout_id,routine_id,user_id):
    u=UserWorkout.query.filter_by(workout_id=workout_id,routine_id=routine_id,user_id=user_id).first()
    if u:
        db.session.delete(u)
        db.session.commit()
        return True
    else:
        return False
    

def viewWorkouts(routine_id,user_id):
    w=UserWorkout.query.filter_by(routine_id=routine_id,user_id=user_id).all()
    print(f'Workouts: {w}')
    if w: 
        workouts=[]
        for i in w:
            work=Workout.query.filter_by(id=i.workout_id).first()
            data=work.to_json()
            data['day']=i.day
            # workouts.append(work.to_json())
            workouts.append(data)
            
        return workouts
    else:
        return None


def changeSets(workout_id,routine_id,user_id,sets):
    u=UserWorkout.query.filter_by(workout_id=workout_id,routine_id=routine_id,user_id=user_id).first()
    if u:
        u.sets=sets
        db.session.commit()
        return True
    else:
        return False


def changeDay(workout_id,routine_id,user_id,day):
    u=UserWorkout.query.filter_by(workout_id=workout_id,routine_id=routine_id,user_id=user_id).first()
    if u:
        u.day=day
        db.session.commit()
        return True
    else:
        return False