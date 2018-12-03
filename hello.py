from flask import Flask, render_template
from wtforms import Form, BooleanField, StringField, PasswordField, validators
import sqlite3

app = Flask(__name__)



@app.route('/')
def hello_world():
    return render_template('index.html')

# @app.route('/')
# def cards():
#     return render_template('cards.html')


if __name__ == '__main__':
    app.run(debug = True)
