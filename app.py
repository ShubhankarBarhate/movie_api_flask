from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy 

app = Flask(__name__)

# Database config
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:manager@localhost/movie_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# Model
class Movie(db.Model):
    __tablename__ = 'movies'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    director = db.Column(db.String(255))
    releaseYear = db.Column(db.Integer)
    genre = db.Column(db.String(100))
    rating = db.Column(db.Float)

    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "director": self.director,
            "releaseYear": self.releaseYear,
            "genre": self.genre,
            "rating": self.rating
        }

# Create tables
with app.app_context():
    db.create_all()

# Routes
@app.route('/')
def home():
    return {"message": "Movie API is running!"}

# GET all movies
@app.route('/movies', methods=['GET'])
def get_movies():
    movies = Movie.query.all()
    return {"movies": [m.to_dict() for m in movies]}

# GET movie by ID (NEW)
@app.route('/movies/<int:id>', methods=['GET'])
def get_movie(id):
    movie = Movie.query.get(id)

    if not movie:
        return {"error": "Movie not found"}, 404

    return movie.to_dict()

# POST movie
@app.route('/movies', methods=['POST'])
def add_movie():
    data = request.get_json()

    if not data:
        return {"error": "Invalid JSON"}, 400

    if not data.get('title'):
        return {"error": "Title is required"}, 400

    if data.get('rating') and not (1 <= data['rating'] <= 10):
        return {"error": "Rating must be between 1 and 10"}, 400

    movie = Movie(
        title=data['title'],
        director=data.get('director'),
        releaseYear=data.get('releaseYear'),
        genre=data.get('genre'),
        rating=data.get('rating')
    )

    db.session.add(movie)
    db.session.commit()

    return {
        "message": "Movie added",
        "movie": movie.to_dict()
    }, 201

# PUT update movie
@app.route("/movies/<int:id>", methods=['PUT'])
def update_movie(id):
    movie = Movie.query.get(id)

    if not movie:
        return {"error": "Movie not found"}, 404

    data = request.get_json()

    if not data:
        return {"error": "Invalid JSON"}, 400

    if data.get('rating') and not (1 <= data['rating'] <= 10):
        return {"error": "Rating must be between 1 and 10"}, 400

    movie.title = data.get('title', movie.title)
    movie.director = data.get('director', movie.director)
    movie.releaseYear = data.get('releaseYear', movie.releaseYear)
    movie.genre = data.get('genre', movie.genre)
    movie.rating = data.get('rating', movie.rating)

    db.session.commit()

    return {
        "message": "Movie updated",
        "movie": movie.to_dict()
    }

# DELETE movie
@app.route('/movies/<int:id>', methods=['DELETE'])
def delete_movie(id):
    movie = Movie.query.get(id)

    if not movie:
        return {"error": "Movie not found"}, 404

    db.session.delete(movie)
    db.session.commit()

    return {"message": "Movie deleted"}, 200

if __name__ == "__main__":
    app.run(debug=True)