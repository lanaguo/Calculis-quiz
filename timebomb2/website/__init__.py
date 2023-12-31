from flask import Flask
from flask_sqlalchemy import SQLAlchemy

DB_NAME = "database.db"

def create_app():
    app = Flask(__name__) #name = name of file, how to initialize flask
    app.config['SECRET_KEY'] = 'sjdkkanbcdkks'
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'

    from .views import views
    from .questions import questions
    
    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(questions, url_prefix='/')

    # from .models import User, Note # need to make sure we run models file so classes r defined b4 we create database
    return app