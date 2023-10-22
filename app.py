from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from views import create_views
from config import create_config


app = Flask(__name__)
create_config(app)
db = SQLAlchemy(app)
create_views(app, db)
