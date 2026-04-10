from flask import Flask
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

if __name__ == "__main__":
    app.run(debug=True)