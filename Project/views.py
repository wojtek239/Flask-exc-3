from flask import render_template, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import DataRequired
from models import db, Movie, Review


class AddMovieForm(FlaskForm):
    title = StringField('Movie Title', validators=[DataRequired()])
    review = TextAreaField('Review', validators=[DataRequired()])
    add = SubmitField('Add Movie')


class AddReviewForm(FlaskForm):
    review = TextAreaField('Review', validators=[DataRequired()])
    add = SubmitField('Add Review')


def index():
    movies = Movie.query.all()
    return render_template('index.html', movies=movies)


def add_movie():
    form = AddMovieForm()

    if form.validate_on_submit():
        title = form.title.data
        review = form.review.data

        new_movie = Movie(title=title)
        db.session.add(new_movie)
        db.session.commit()

        new_review = Review(content=review, movie_id=new_movie.id)
        db.session.add(new_review)
        db.session.commit()

        return redirect(url_for('index'))

    return render_template('add_movie.html', form=form)


def summary():
    movies = Movie.query.all()
    return render_template('summary.html', movies=movies)
