from flask import Flask
from views import index, add_movie, summary
from models import init_db
import os
import random

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'

app.config['SECRET_KEY'] = os.urandom(16).hex()
print("CSRF Key:", app.config['SECRET_KEY'])

init_db(app)


app.add_url_rule('/', 'index', index)
app.add_url_rule('/add_movie', 'add_movie', add_movie, methods=['GET', 'POST'])
app.add_url_rule('/summary', 'summary', summary)

if __name__ == "__main__":
    app.run(debug=True)
