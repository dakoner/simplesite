from bs4 import BeautifulSoup
import pytest
from app import app


@pytest.fixture
def client():
    with app.test_client() as client:
        yield client


def test_index(client):
    rv = client.get('/')
    assert rv.status_code == 200
    bs = BeautifulSoup(rv.data, "html.parser")
    assert bs.head is not None
    assert bs.body is not None


def test_missing(client):
    rv = client.get('/thispagedoesnotexist')
    assert rv.status_code == 404

