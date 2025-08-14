from flask import jsonify, request, render_template
from flask import Blueprint, render_template, url_for, request, session, redirect, Flask, jsonify, flash, make_response
from google.cloud import storage, vision
from werkzeug.utils import secure_filename
import io
import json
import datetime
import hashlib
import random
import string
import os
import google.generativeai as palm
from google.cloud import storage
from google.cloud import datastore
import requests
import re
import random
from website.keywords import clothing_keywords, color_keywords
from flask_cors import CORS

config_file = os.getenv('CONFIG_FILE')

print(f"The value of CONFIG_FILE is: {config_file}")

with open(config_file) as f:
    config = json.load(f)



views = Blueprint('views', __name__)
CORS(views)

storage_client = storage.Client()

@views.route('/health', methods=['GET'])
def get_service_health():

    response = {
      "status": "healthy",     
      "app_name": "claimletter",     
      "status_code":200
                }
        
    return jsonify(response), 200


@views.route('/')
def claimletter():

    return render_template('claimletter.html')

@views.route('/generate_letter', methods=['POST'])
def generate_letter():
    # Get the JSON data sent by JavaScript
    data = request.json

    # Extract the claimRequestForm data
    claim_request_form = data.get('claimRequestForm')
    print("Received claimRequestForm data:", claim_request_form)

    if claim_request_form:
        # Create a JSON payload with the claimRequestForm data
        payload = {'claimRequestForm': claim_request_form}

        # Define the URL of your Cloud Run API
        endpoint = '/generate_claim_letter'
        api_url = f"{config['BASE_URL']}{endpoint}"

        # Send the JSON payload to your Cloud Run API
        response = requests.post(api_url, json=payload)

        # Get the API response
        api_response = response.json()

        # Return the API response as JSON
        return jsonify(api_response)

    # If claimRequestForm is not found in the JSON data, return an error response
    return jsonify({'error': 'claimRequestForm not found'})
