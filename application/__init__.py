from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = 'db5821567f7f382d2883960140f805c2da33e9bffd7b78d6'

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://c1945047:Lancometer3!@csmysql.cs.cf.ac.uk:3306/c1945047_Team18Portfolio'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = 1
db = SQLAlchemy(app)

from application.models import Job

from application import routes

