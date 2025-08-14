import pytest
from flask import Flask, jsonify
import os
from main import create_app

@pytest.fixture
def app():
    app = create_app()
    app.config['TESTING'] = True
    yield app

@pytest.fixture
def client(app):
    return app.test_client()

def test_health_route(client):
    response = client.get('/health')
    assert response.status_code == 200
    data = response.get_json()
    assert data['status'] == 'healthy'
    assert data['app_name'] == 'styleme'

def test_styleme_get_route(client):
    response = client.get('/')
    assert response.status_code == 200
    # Add more assertions for the expected behavior

def test_styleme_post_route(client):
    data = {
        "conversation": ["User: Hello", "Fashion Assistant: Hi!"],
        "persona": "User's Persona"
    }
    response = client.post('/', json=data)
    assert response.status_code == 200
    # Add more assertions for the expected behavior

def test_styleme_qna_route(client):
    data = {
        "persona": "User's Persona",
        "question": "What's the latest fashion trend?"
    }
    response = client.post('/stylemeqna', json=data)
    assert response.status_code == 200
    data = response.get_json()
    assert 'answer' in data
    # Add more assertions for the expected behavior



