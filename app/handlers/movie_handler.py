from flask import Blueprint, request
from app.services import movie_service

movie_bp = Blueprint("movies", __name__)

@movie_bp.route('/', methods=['GET'])
def home():
    return {"message": "Movie API is running!"}


#  GET ALL MOVIES
@movie_bp.route('/movies', methods=['GET'])
def get_movies():
    """
    Get all movies
    ---
    responses:
      200:
        description: List of movies
    """
    movies = movie_service.get_movies()
    return {"movies": [m.to_dict() for m in movies]}


#  GET MOVIE BY ID
@movie_bp.route('/movies/<int:id>', methods=['GET'])
def get_movie(id):
    """
    Get movie by ID

    parameters:
      - name: id
        in: path
        type: integer
        required: true
    responses:
      200:
        description: Movie found
      404:
        description: Movie not found
    """
    movie = movie_service.get_movie(id)

    if not movie:
        return {"error": "Movie not found"}, 404

    return movie.to_dict()


#  ADD MOVIE
@movie_bp.route('/movies', methods=['POST'])
def add_movie():
    """
    Add a new movie
    ---
    parameters:
      - name: body
        in: body
        required: true
        schema:
          type: object
          properties:
            title:
              type: string
            director:
              type: string
            releaseYear:
              type: integer
            genre:
              type: string
            rating:
              type: number
    responses:
      201:
        description: Movie created
      400:
        description: Validation error
    """
    data = request.get_json()
    result = movie_service.add_movie(data)

    if isinstance(result, tuple):
        return result

    return {"message": "Movie added", "movie": result.to_dict()}, 201


#  UPDATE MOVIE
@movie_bp.route('/movies/<int:id>', methods=['PUT'])
def update_movie(id):
    """
    Update movie
    ---
    parameters:
      - name: id
        in: path
        type: integer
        required: true
      - name: body
        in: body
        required: true
        schema:
          type: object
    responses:
      200:
        description: Movie updated
      404:
        description: Movie not found
    """
    data = request.get_json()
    result = movie_service.update_movie(id, data)

    if isinstance(result, tuple):
        return result

    return {"message": "Movie updated", "movie": result.to_dict()}


#  DELETE MOVIE
@movie_bp.route('/movies/<int:id>', methods=['DELETE'])
def delete_movie(id):
    """
    Delete movie
    ---
    parameters:
      - name: id
        in: path
        type: integer
        required: true
    responses:
      200:
        description: Movie deleted
      404:
        description: Movie not found
    """
    result = movie_service.delete_movie(id)

    if isinstance(result, tuple):
        return result

    return {"message": "Movie deleted"}