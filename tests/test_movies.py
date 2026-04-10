import pytest
from app.main import create_app
from app.database import db

@pytest.fixture
def client():
    app = create_app()

    # Override config for testing
    app.config['TESTING'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///:memory:"

    with app.test_client() as client:
        with app.app_context():
            db.create_all()
        yield client