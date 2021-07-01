import os

import pytest

from app import create_app

@pytest.fixture
def client():
    app = create_app() #{'TESTING': True, 'DATABASE': db_path})

    with app.test_client() as client:
        # with app.app_context():
        #     init_db()
        yield client

