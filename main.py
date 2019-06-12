from flask import Flask, request, redirect, render_template, session, flash
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['DEBUG'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql_pymysql://field-map:field-map@localhost:3306/field-map'
app.config['SQLALCHEMY_ECHO'] = True
db = SQLAlchemy(app)

app.secret_key = 'secret_key'

#list of dictionaries that we pull our data from in the html forms. 
#will take the place of database for now
posts = [
    {
        'author': 'Edward Prenzler',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'June 11, 2019'
    },
    {
        'author': 'Ryan Theis',
        'title': 'Blog Post 2',
        'content': 'Next blog post',
        'date_posted': 'June 11, 2019'
    }
]

@app.route('/')
@app.route('/map')
def index():
    return "Looks like this baby is up n running"

@app.route('/home')
def home():
    return render_template('home.html', posts=posts)

@app.route("/about")
def about():
    return render_template('about.html', title='About')

if __name__ == '__main__':
    app.run()
