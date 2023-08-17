# from flask import Flask, render_template, url_for
# app = Flask(__name__)

# @app.route('/')
# def home():
#     return render_template('max.html')

from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from model import Task

app = Flask(__name__)
@app.route('/')
def index():
    tasks = Task.query.all()
    return render_template('index.html', tasks=tasks)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///todo.db'
db = SQLAlchemy(app)
