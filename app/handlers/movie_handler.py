from flask import Blueprint, request
from app.services import movie_service

movie_bp = Blueprint("movies", __name__)

@movie_bp.route('/', methods=['GET'])
def home():
    return {"message": "Movie API is running!"}

@movie_bp.route('/movies/<int:id>', methods=['GET'])
def get_movie(id):
    movie = movie_service.get_movie(id)

    if not movie:
        return {"error": "Movie not found"}, 404

    return movie.to_dict()

@movie_bp.route('/movies', methods=['POST'])
def add_movie():
    data = request.get_json()
    result = movie_service.add_movie(data)

    if isinstance(result, tuple):
        return result

    return {"message": "Movie added", "movie": result.to_dict()}, 201

@movie_bp.route('/movies/<int:id>', methods=['PUT'])
def update_movie(id):
    data = request.get_json()
    result = movie_service.update_movie(id, data)

    if isinstance(result, tuple):
        return result

    return {"message": "Movie updated", "movie": result.to_dict()}

@movie_bp.route('/movies/<int:id>', methods=['DELETE'])
def delete_movie(id):
    result = movie_service.delete_movie(id)

    if isinstance(result, tuple):
        return result

    return {"message": "Movie deleted"}