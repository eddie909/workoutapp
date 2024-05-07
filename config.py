from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS 
import os
from dotenv import load_dotenv
from flask_migrate import Migrate
load_dotenv()


app = Flask(__name__) 
CORS(app) 


app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mydatabase.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY']=os.getenv('SECRET_KEY')
app.config['API_KEY']=os.getenv('API_KEY')
app.config['JWT_SECRET_KEY']=os.getenv('JWT_SECRET')
app.config['JWT_TOKEN_LOCATION']=['cookies']
app.config['JWT_COOKIE_CSRF_PROTECT']=False
app.config['WTF_CSRF_ENABLED']=False
# CSRFProtect(app)

db = SQLAlchemy(app)


Migrate(app,db)

#import secrets
# secret_key = secrets.token_hex(25)
# print(secret_key)