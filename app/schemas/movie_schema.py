def validate_movie(data):
    if not data:
        return "Invalid JSON"

    if not data.get("title"):
        return "Title is required"

    if 'rating' in data and not (1 <= data['rating'] <= 10):
        return "Rating must be between 1 and 10"

    if 'releaseYear' in data and not isinstance(data['releaseYear'], int):
        return "releaseYear must be integer"

    return None