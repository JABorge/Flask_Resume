from email.errors import FirstHeaderLineIsContinuationDefect
from flask import Flask, render_template

app = Flask(__name__)

# CREATE INDEX PAGE
@app.route('/')
def index():
    first_name = 'John'
    favorite_pizza = ["Pepperoni", "Cheese", "Supreme", "Mushroom"]
    return render_template('index.html', 
        first_name=first_name, 
        favorite_pizza=favorite_pizza)


# CREATE ABOUT PAGE
@app.route('/about')
def about():
    return render_template('about.html')