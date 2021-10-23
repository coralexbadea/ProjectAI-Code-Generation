from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path
from flask_login import LoginManager
from flask_cors import CORS

db = SQLAlchemy()
DB_NAME = "database.db"


def create_app():
    app = Flask(__name__)
    CORS(app)

    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SECRET_KEY'] = 'hjshjhdjah kjshkjdhjs'
    #app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    #app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:scoala3@localhost/flask'
    #app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:@localhost/projectai'
    
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://pldhmkigshikio:8b2bcd8105ad752fd4b7df587782d83e29b7906184b7f7d3b876dfc948be3866@ec2-34-233-187-36.compute-1.amazonaws.com:5432/d1njldibcu6pts'
    
   

    db.init_app(app)

    from .controllers.authController import auth
    from .controllers.nlpController import nlp

    app.register_blueprint(auth, url_prefix='/')
    app.register_blueprint(nlp, url_prefix='/nlp')

    from .models import User

    #create_database(app)

    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)
    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))

    return app


def create_database(app):
    db.create_all(app=app)     
