from flask import Flask
from flask_bootstrap import Bootstrap
app = Flask(__name__)
bootstrap = Bootstrap(app)

from flask_sqlalchemy import SQLAlchemy

import os
if os.environ.get("HEROKU"):
    app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("DATABASE_URL")
else:
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///invoice.db"    
    app.config["SQLALCHEMY_ECHO"] = True

db = SQLAlchemy(app)

from application import views

from application.customer import models
from application.customer import views

from application.product import views
from application.invoice import views

from application.auth import models 
from application.auth import views

from application.auth.models import User
from os import urandom
app.config["SECRET_KEY"] = urandom(32)

from flask_login import LoginManager
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "auth_login"
login_manager.login_message = "Please login to use this functionality."

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)

@app.template_filter('datetime')
def datetimeformat(value, format='%d.%m.%Y'):
    return value.strftime(format)

try: 
    db.create_all()
    # u = User("Erkki", "erkki", "sala")
    # db.session().add(u)
    # db.session().commit()
    # u = User("Paavo", "paavo", "sala")
    # db.session().add(u)
    # db.session().commit()
except:
    pass