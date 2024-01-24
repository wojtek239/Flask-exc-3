from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from views import index, add_movie, summary

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///baza.db'
db = SQLAlchemy(app)


app.add_url_rule('/', 'index', index)
app.add_url_rule('/add_movie', 'add_movie', add_movie, methods=['GET', 'POST'])
app.add_url_rule('/summary', 'summary', summary)

if __name__ == "__main__":
    app.run(debug=True)
