from models import Routine
from config import db

def getRoutine(id,user_id):
    return Routine.query.filter_by(id=id,user_id=user_id).first()

def createRoutine(name,user_id):
    r = Routine.query.filter_by(name=name).first()
    if r:
        return None
    else:
        r = Routine(name=name, user_id=user_id)
        db.session.add(r)
        db.session.commit()
        return r
    
def editRoutine(name, workout_id):
    r= Routine.query.filter_by(name=name).first()
    if r:
        r = Routine(name, workout_id)
        r.name = name
        db.session.commit()
        return True
    else:
        return False

def deleteRoutine(id):
    r = Routine.query.filter_by(id=id).first()
    
    if r:
        db.session.delete(r)
        db.session.commit() 
        return True
    else:
        return False

def getRoutines(user_id):
    return Routine.query.filter_by(user_id=user_id).all()
   


def renameRoutine(name, new_name):
    r = Routine.query.filter_by(name=name).first()
    if not r:
        return False
    else:
        r.name = new_name
        db.session.commit()
        return True

def getRoutineCount(user_id):
    return Routine.query.filter_by(user_id=user_id).count()