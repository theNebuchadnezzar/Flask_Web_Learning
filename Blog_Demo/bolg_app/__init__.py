# -*- coding:utf-8 -*-
from flask import Flask,render_template
from flask.ext.bootstrap import Bootstrap
from flask.ext.mail import Mail
from flask.ext.moment import Moment
from flask.ext.sqlalchemy import  SQLAlchemy
from config import config

bootstrap = Bootstrap()
mail = Mail
moment = Moment
db = SQLAlchemy

def creat_app(config_name):
    blog_app = Flask (__name__)
    blog_app.config.from_object(config[config_name])
    config[config_name].init_app(blog_app)

    bootstrap.init_app(blog_app)
    mail.init_app(blog_app)
    moment.init_app(blog_app)
    db.init_app(blog_app)

    #附加路由和自定义错误界面
    from .main import  main as main_blueprint
    blog_app.register_blueprint(main_blueprint)

    return blog_app
