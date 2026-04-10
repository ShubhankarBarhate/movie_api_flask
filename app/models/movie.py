from app.database import db

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