from flask_jwt_extended import create_access_token,JWTManager
from models import User
from config import app
from datetime import timedelta
from flask import request,redirect,flash
from functools import wraps

jwt=JWTManager(app)


# JWT Config to enable current_user
@jwt.user_identity_loader
def user_identity_lookup(user):
  return user.id

@jwt.user_lookup_loader
def user_lookup_callback(_jwt_header, jwt_data):
  identity = jwt_data["sub"]
  return User.query.get(identity) # Must return None if user not found


def login_user(username, password):
  user = User.query.filter_by(username=username).first()
  if user and user.check_password(password):
    expires = timedelta(minutes=60) # Token expires in 10 minutes
    token = create_access_token(identity=user, expires_delta=expires) 
    return token
  return None


# def is_token_expired(token):
#     try:
#         jwt.decode(token, app.config['SECRET_KEY'], algorithms=['HS256'], verify_exp=True)
#         return False
#     except jwt.ExpiredSignatureError:
#         return True


"""
Decorator to check if token is expired
"""
# def token_required(f):
#   @wraps(f)
#   def decorated_function(*args, **kwargs):
#     token = request.cookies.get('token')
#     print(f'Token: {token}')
#     if token and not is_token_expired(token):
#       return f(*args, **kwargs)
#     else:
#       flash('Token expired','error')
#       return redirect('/')
#   return decorated_function

@jwt.expired_token_loader
def expired_token_callback(jwt_header, jwt_payload):
    return redirect('/')

