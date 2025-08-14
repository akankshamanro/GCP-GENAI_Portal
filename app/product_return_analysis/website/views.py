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
      "app_name": "product_return_analysis",   
      "status_code":200
                }
        
    return jsonify(response), 200

storage_client = storage.Client()

@views.route('/')
def product_return_analysis():

    return render_template('product_return_analysis.html')


# Initialize generated_text as a global variable
generated_text = None

@views.route('/submit_complaint', methods=['POST'])
def submit_complaint():
    global generated_text  # Access the global variable

    # Get the complaint text from the request
    complaint_text = request.json.get('complaintText')
    
    if not complaint_text:
        return jsonify({"error": "Complaint text is empty"})

    try:
        
        data = {"complaintText": complaint_text}
       
        endpoint = '/submit_complaint'
        
        api_url = f"{config['BASE_URL']}{endpoint}"

        # Send a POST request to your Cloud Run service with the correct content type
        response_post = requests.post(api_url, json=data, headers={"Content-Type": "application/json"})

        if response_post.status_code == 200:
            response_data = response_post.json()
            generated_text = response_data.get("generated_text", "No text generated.")
            print(f"Generated Text: {generated_text}")  # Log the generated text
            print(generated_text)
            # Store the generated_text in the global variable
            # session['generated_text']= generated_text
            
            return jsonify({"generated_text": generated_text})  # Return generated_text in JSON response

        else:
            print(f"POST request to Cloud Run service failed with status code: {response_post.status_code}")
            return jsonify({"error": "POST request to Cloud Run service failed"})

    except Exception as e:
        print(f"Error in Flask route: {str(e)}")
        return jsonify({"error": str(e)})


@views.route('/product_return_summary', methods=['GET', 'POST'])
def product_return_summary():
    global generated_text  # Access the global variable

    if generated_text and isinstance(generated_text, dict):
        # Extract relevant data from the stored_generated_text dictionary
        product_id = generated_text.get("product_id", "")
        product_name = generated_text.get("product_name", "")
        issue = generated_text.get("issue", "")
        print(generated_text)
        # Create a dictionary containing the product information
        productData = {
            "product_id": product_id,
            "product_name": product_name,
            "returns": 1,  # Set a default value for returns
            "issue": issue
        }

        return jsonify(productData)  # Return product data as JSON

    else:
        # If no data is available, return an empty dictionary
        return jsonify({})


@views.route('/generate_complaint_email', methods=['POST'])
def generate_complaint_email():
    try:
        # Extract the row data from the request
        row_data = request.json.get('rowData')

        if not row_data:
            return jsonify({"error": "Row data is empty"})

        # Create a request payload to send to your Cloud Run service
        payload = {"productData": row_data}
        
        endpoint = '/generate_complaint_email'
        api_url = f"{config['BASE_URL']}{endpoint}"

        # Send a POST request to your Cloud Run service with the correct content type
        response_post = requests.post(api_url, json=payload, headers={"Content-Type": "application/json"})

        if response_post.status_code == 200:
            response_data = response_post.json()
            generated_complaint_email = response_data.get("complaintEmail", "No email generated.")
            print(f"Generated Complaint Email: {generated_complaint_email}")  # Log the generated email

            # Return the generated email as a response
            return jsonify({"complaintEmail": generated_complaint_email})

        else:
            print(f"POST request to Cloud Run service failed with status code: {response_post.status_code}")
            return jsonify({"error": "POST request to Cloud Run service failed"})

    except Exception as e:
        print(f"Error in Flask route: {str(e)}")
        return jsonify({"error": str(e)})


