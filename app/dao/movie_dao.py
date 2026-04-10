from app.models.movie import Movie
from app.database import db

def get_all_movies():
    return Movie.query.all()

def get_movie_by_id(movie_id):
    return db.session.get(Movie, movie_id)

def create_movie(data):
    movie = Movie(**data)
    db.session.add(movie)
    db.session.commit()
    return movie

def update_movie(movie, data):
    for key, value in data.items():
        setattr(movie, key, value)
    db.session.commit()
    return movie

def delete_movie(movie):
    db.session.delete(movie)
    db.session.commit()