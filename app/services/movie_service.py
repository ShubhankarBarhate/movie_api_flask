from app.dao import movie_dao
from app.schemas.movie_schema import validate_movie

def get_movies():
    return movie_dao.get_all_movies()

def get_movie(movie_id):
    return movie_dao.get_movie_by_id(movie_id)

def add_movie(data):
    error = validate_movie(data)
    if error:
        return {"error": error}, 400

    return movie_dao.create_movie(data)

def update_movie(movie_id, data):
    movie = movie_dao.get_movie_by_id(movie_id)

    if not movie:
        return {"error": "Movie not found"}, 404

    error = validate_movie(data)
    if error:
        return {"error": error}, 400

    return movie_dao.update_movie(movie, data)

def delete_movie(movie_id):
    movie = movie_dao.get_movie_by_id(movie_id)

    if not movie:
        return {"error": "Movie not found"}, 404

    movie_dao.delete_movie(movie)
    return True