# app/views.py
from flask import Flask, render_template, redirect, url_for
from .forms import AddMovieForm, AddOpinionForm
from .models import db, Movie, Opinion

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///base.db'
db.init_app(app)

with app.app_context():
    db.create_all()


@app.route('/')
def index():
    movies = Movie.query.all()
    return render_template('index.html', movies=Movie)


@app.route('/add_movie', methods=['GET', 'POST'])
def add_movie():
    form = AddMovieForm()

    if form.validate_on_submit():
        title = form.title.data
        opinion = form.opinion.data

        new_movie = Movie(title=title)
        db.session.add(new_movie)
        db.session.commit()

        new_opinion = Opinion(content=opinion, movie_id=new_movie.id)
        db.session.add(new_opinion)
        db.session.commit()

        return redirect(url_for('index'))

    return render_template('add_movie.html', form=form)


@app.route('/summary')
def summary():
    filmy = Movie.query.all()
    return render_template('summary.html', movies=Movie)
