from flask import Flask
from app.database import db
from app.handlers.movie_handler import movie_bp
import os
from flasgger import Swagger
from dotenv import load_dotenv

load_dotenv()  # Load .env

def create_app():
    app = Flask(__name__)

    db_url = os.getenv("DATABASE_URL")
    if not db_url:
        raise ValueError("DATABASE_URL is not set in .env")

    app.config['SQLALCHEMY_DATABASE_URI'] = db_url
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)
    Swagger(app)

    with app.app_context():
        db.create_all()

    app.register_blueprint(movie_bp)

    return app

app = create_app()

if __name__ == "__main__":
    app.run(debug=os.getenv("FLASK_DEBUG") == "True")