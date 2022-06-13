from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
db = SQLAlchemy(app)


@app.route("/")

@app.route('/home')
def home_page():
    return render_template('home.html')

@app.route('/market')
def market_page():
    items = [
    {'number': 1, 'title': 'Sales Assosiciate', 'education': 'Junior High School', 'salary': 20},
    {'number': 2, 'title': 'Network Engineer', 'education': 'High School', 'salary': 24},
    {'number': 3, 'title': 'Sanitation Tech/KTB', 'education': 'Bachelors Degree', 'salary': 27}
]
    return render_template('market.html', items=items)

@app.route('/ml_before')
def ml_before_page():
    return render_template ('ml_before')







