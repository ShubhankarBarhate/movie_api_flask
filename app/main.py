from flask import Flask
from app.database import db
from app.handlers.movie_handler import movie_bp
import os
from flasgger import Swagger
from dotenv import load_dotenv

load_dotenv(os.path.join(os.path.dirname(__file__), ".env"))  # Load app/.env

def create_app(test_config=None):
    app = Flask(__name__)

    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv("DATABASE_URL")
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    if test_config:
        app.config.update(test_config)

    if not app.config['SQLALCHEMY_DATABASE_URI']:
        raise ValueError("DATABASE_URL is not set in .env")

    db.init_app(app)
    Swagger(app)

    with app.app_context():
        db.create_all()

    app.register_blueprint(movie_bp)

    return app

if __name__ == "__main__":
    app = create_app()
    app.run(debug=os.getenv("FLASK_DEBUG") == "True")
