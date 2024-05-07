from models import User
from config import db


def getUser(username):
    user = User.query.filter_by(username=username.lower()).first()
    return user

def createUser(username, password):
    user = User(username=username, password=password)
    db.session.add(user)
    db.session.commit()
    return user

def getUsers():
    users = User.query.all()
    return users

def getUserById(id):
    user = User.query.filter_by(id=id).first()
    return user