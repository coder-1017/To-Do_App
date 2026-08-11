from flask import Flask 
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv
import os 

load_dotenv()

app = Flask(__name__)

app.config["SECRET_KEY"] = os.getenv("SECRET_KEY","dev-fallback-key-change-in-production")
app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///todo.db'

db = SQLAlchemy(app)

from app import routes
#routes is imported at the end to prevent circular import error 


