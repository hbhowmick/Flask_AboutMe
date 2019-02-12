# import app variable instance in order to run application
# also import necessary flask methods
from app import app
from flask import render_template, url_for



# create route for index page, render index.html file
@app.route('/')
@app.route('/index')
@app.route('/index', methods=['GET'])
# @app.route('/index/<name>', methods=['GET'])
def index():
    heading = 'Welcome'
    hobbies = ['Avid dog cuddling', 'Creative cartography', 'Red-blend wine testing', 'Competing on Chopped: Lawrence edition', 'Occasional rock climbing']
    return render_template('index.html', title='Home', heading=heading, hobbies=hobbies)



@app.route('/about_me', methods=['GET'])
def about_me():
    heading = 'Heather Bhowmick'
    return render_template('about_me.html', title='About Me', heading=heading)
