import pytest
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_index_page(client):
    """Test if the index page loads correctly"""
    rv = client.get('/')
    assert rv.status_code == 200
    assert b'ACEestFitness and Gym' in rv.data

def test_add_workout_success(client):
    """Test adding a valid workout"""
    response = client.post('/add_workout', data={
        'workout': 'Running',
        'duration': '30'
    }, follow_redirects=True)
    assert response.status_code == 200
    assert b'Running' in response.data
    assert b'added successfully' in response.data

def test_add_workout_missing_fields(client):
    """Test adding a workout with missing fields"""
    response = client.post('/add_workout', data={
        'workout': '',
        'duration': ''
    }, follow_redirects=True)
    assert response.status_code == 200
    assert b'Please enter both workout and duration' in response.data

def test_add_workout_invalid_duration(client):
    """Test adding a workout with invalid duration"""
    response = client.post('/add_workout', data={
        'workout': 'Running',
        'duration': 'invalid'
    }, follow_redirects=True)
    assert response.status_code == 200
    assert b'Duration must be a number' in response.data
