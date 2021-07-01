from bs4 import BeautifulSoup
import pytest
from main import create_app


@pytest.fixture
def client():
    app = create_app()

    with app.test_client() as client:
        yield client


def test_root(client):
    rv = client.get('/')
    assert rv.status_code == 302
    assert rv.headers['Location'].endswith("/static/index.html")


def test_missing(client):
    rv = client.get('/thispagedoesnotexist')
    assert rv.status_code == 404


def test_index(client):
    rv = client.get('/static/index.html')
    assert rv.status_code == 200
    bs = BeautifulSoup(rv.data, "html.parser")
    assert bs.head is not None
    assert bs.body is not None
