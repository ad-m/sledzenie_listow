from flask_wtf import Form
from wtforms import TextField
from wtforms.validators import DataRequired


class SearchForm(Form):
    start = TextField('Start', validators=[DataRequired()])
    end = TextField('End', validators=[DataRequired()])
