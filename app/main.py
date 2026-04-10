from flask import Flask
from app.database import db
from app.handlers.movie_handler import movie_bp
import os

def create_app():
    app = Flask(__name__)

    # Database config
    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv(
        "DATABASE_URL",
        "mysql+pymysql://root:manager@localhost/movie_db"
    )
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # Initialize DB
    db.init_app(app)

    # Create tables
    with app.app_context():
        db.create_all()

    # Register routes
    app.register_blueprint(movie_bp)

    return app

app = create_app()

if __name__ == "__main__":
    app.run(debug=True)