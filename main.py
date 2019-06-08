from flask import Flask, request, redirect, render_template, session, flash
#from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['DEBUG'] = True
#app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql_pymysql://field-map:field-map@localhost:3306/field-map'
#app.config['SQLALCHEMY_ECHO'] = True
#db = SQLAlchemy(app)

#app.secret_key = 'secret_key'

@app.route('/')
def index():
    #return redirect('/blog')
    return "Looks like this baby is up n running"



app.run()
