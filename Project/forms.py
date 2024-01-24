from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import DataRequired


class AddMovieForm(FlaskForm):
    title = StringField('movie title', validators=[DataRequired()])
    opinion = TextAreaField('opinion', validators=[DataRequired()])
    add = SubmitField('add movie')


class AddOpinionForm(FlaskForm):
    opinion = TextAreaField('opinion', validators=[DataRequired()])
    add = SubmitField('add opinion')
