import os
import sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'site-packages'))

from flask import Flask
from flask_bootstrap import Bootstrap
from flask_mail import Mail
from flask_moment import Moment
from flask_sqlalchemy import  SQLAlchemy
from config import config
from flask_login import LoginManager

bootstrap = Bootstrap()
mail = Mail()
moment = Moment()
db = SQLAlchemy()
login_manager = LoginManager()
login_manager.session_protection = 'strong'
login_manager.login_view = 'auth.login'

def creat_app(config_name):
    blog_app = Flask(__name__)
    blog_app.config.from_object(config[config_name])
    config[config_name].init_app(blog_app)

    bootstrap.init_app(blog_app)
    mail.init_app(blog_app)
    moment.init_app(blog_app)
    db.init_app(blog_app)
    login_manager.init_app(blog_app)

    from .main import main as main_blueprint
    blog_app.register_blueprint(main_blueprint)

    from .auth import auth as auth_blueprint
    blog_app.register_blueprint(auth_blueprint, url_prefix='/auth')

    return blog_app
