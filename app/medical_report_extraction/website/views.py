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

@views.route('/health', methods=['GET'])
def get_service_health():

    response = {
      "status": "healthy",     
      "app_name": "medical_report_extraction",
      "status_code":200
                }
        
    return jsonify(response), 200

storage_client = storage.Client()


@views.route('/')
def medical_report_extraction():

    return render_template('medical_report_extraction.html')


@views.route('/extract_medreport_info', methods=['POST'])  # Only accept POST requests
def extract_medreport_info():
    # Get the medical report text from the JSON data sent by JavaScript
    data = request.json
    medical_report = data.get('medical_report')

    if medical_report:
        # Create a JSON payload with the medical report
        payload = {'content': medical_report}

        endpoint = '/service/ai/extract_medreport_info'
        api_url = f"{config['BASE_URL']}{endpoint}"

        # Send the JSON payload to your Cloud Run API
        response = requests.post(api_url, json=payload)

        # Get the API response
        api_response = response.json()
        print(api_response)
        # Return the API response as JSON
        return jsonify(api_response)

    # If medical_report is not found in the JSON data, return an error response
    return jsonify({'error': 'Medical report not provided'})
