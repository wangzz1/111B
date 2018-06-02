# -*- coding: UTF-8 -*-
import datetime,os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
import views

basedir = os.path.abspath(os.path.dirname(__file__))
app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'+ os.path.join(basedir,'blog.sqlite')
db = SQLAlchemy(app)

manager = Manager(app)

class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer,primary_key=True)
    username = db.Column(db.Integer,unique=True)
    password = db.Column(db.String(200),unique=True)


class Blog(db.Model):
    __tablename__ = 'blog'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50),unique=True)
    time = db.Column(db.DateTime,index=True,default=datetime.datetime.now())
    note = db.Column(db.String(100),unique=True)
    content = db.Column(db.Text)
migrate = Migrate(app,db)
manager.add_command('db',MigrateCommand)

if __name__ == '__main__':
    manager.run()