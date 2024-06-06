# Basic app to fetch and display information from a database in the terminal using Python/Flask/SQLAlchemy
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import text

app = Flask(__name__)  # creating an instance of the Flask Class

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:Ponderosa@localhost/movies_example'  # This db code stays in the app file. Tells app where to get the db.
app.config['SQLALCHEMY_ECHO'] = True  # Display the generated SQL commands.

db = SQLAlchemy(app) 

@app.route('/')
def home():
    with app.app_context():
              query = text("SELECT * FROM movies")
              movies = db.session.execute(query).all()
              print(movies)
              return render_template('home.html')

# Start the Flask development server
if __name__ == '__main__':
    app.run()