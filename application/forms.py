from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField
from wtforms.validators import InputRequired

class SearchForm(FlaskForm):
    search_job = StringField('Search', validators=[InputRequired()])
    search = SubmitField('Search')

