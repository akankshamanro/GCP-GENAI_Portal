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
    assert 'status' in data
    assert 'app_name' in data


def test_medical_report_extraction_route(client):
    
    data = {
        "medical_report": "This is a sample medical report text."
    }

    response = client.post('/extract_medreport_info', json=data)
    assert response.status_code == 200
    response_data = response.get_json()

    # Assert that 'extracted_info' is in the response data
    assert 'extracted_info' in response_data

    extracted_info = response_data.get('extracted_info', '')
    assert "hypertension" in extracted_info
    assert "diabetes" in extracted_info
   



