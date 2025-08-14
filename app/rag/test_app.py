import pytest
from flask import Flask, jsonify, json
import os
from main import create_app

@pytest.fixture
def app():
    app = create_app()
    app.config['TESTING'] = True
    yield app

def test_medicalComparision_route(client):
    response = client.get('/')
    assert response.status_code == 200
