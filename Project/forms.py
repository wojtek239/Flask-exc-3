from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import DataRequired


class AddMovieForm(FlaskForm):
    title = StringField('Movie Title', validators=[DataRequired()])
    review = TextAreaField('Review', validators=[DataRequired()])
    add = SubmitField('Add Movie')


class AddReviewForm(FlaskForm):
    review = TextAreaField('Review', validators=[DataRequired()])
    add = SubmitField('Add Review')
