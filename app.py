from flask import Flask
from flask import Flask,request

app = Flask(__name__)

movies = [
    {"id": 1, "title": "The Shawshank Redemption", "director": "Frank Darabont", "year": 1994},
    {"id": 2, "title": "The Godfather", "director": "Francis Ford Coppola", "year": 1972},
    {"id": 3, "title": "The Dark Knight", "director": "Christopher Nolan", "year": 2008}
]
@app.route('/')
def home():
    return {"message": " Movie API is running!"}
@app.route('/movies', methods=['GET'])
def get_movies():
    return {"movies": movies}

@app.route('/movies',methods=['POST'])
def add_movie():
    new_movie =request.json
    movies.append(new_movie)
    return{"message":"Movie added","movie":new_movie}

@app.route("/movies/<int:id>", methods=[PUT])
def update_movie(id):
    for movie in movies:
        if movie["id"] == id:
            movie.update(request.json)
            return {"message":"Movie updated", "movie":movie}
    return {"massage":"Movie not found"}

@app.route('/movies/<int:id>', methods=['DELETE'])
def delete_movie(id):
    for movie in movies:
        if movie["id"] == id:
            movies.remove(movie)
            return {"message": "Movie deleted"}
    return {"message": "Movie not found"}

if __name__ == "__main__":
    app.run(debug=True)