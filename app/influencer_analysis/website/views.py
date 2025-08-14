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
      "app_name": "influencer_analysis",  
      "status_code":200
                }
        
    return jsonify(response), 200


# Initialize last_generated_id to 0 at the beginning of your script
last_generated_id = 0

# Function to give random celebrity id from range
def generate_random_celeb_id():
    global last_generated_id  # Access the global variable

    # Define the range of celebrity IDs
    start_id = 1
    end_id = 22  # Adjust this to the desired end ID

    # Increment the last generated ID
    last_generated_id += 1

    # Check if we have reached the end ID, and loop back to the start if needed
    if last_generated_id > end_id:
        last_generated_id = start_id

    # Create the next celebrity ID
    celeb_id = f"celeb_{str(last_generated_id).zfill(3)}"

    # Return the generated celebrity ID
    return celeb_id


@views.route('/')
def influencer_analysis():
    

    return redirect('/influencersalesanalysis')


@views.route('/influencersalesanalysis')
def influencersalesanalysis():

    # app_name = request.args.get('app_name')
    # team_members_info = get_team_members_by_app_name(app_name)

    # if team_members_info:
    #     for member in team_members_info:
    #         print(f"Name: {member['name']}, Role: {member['role']}")
    # else:
    #     print(f"No team members found for {app_name}")

    endpoint = '/service/celebrity/celebrity_id'
    api_url = f"{config['BASE_URL']}{endpoint}"

    # Example usage:
    random_celeb_id = generate_random_celeb_id()
    print(random_celeb_id)
    session['celebrity_id'] = random_celeb_id

    response = requests.post(api_url,json={"celebrity_id": random_celeb_id})
    print(response.json())

    celeb_data = response.json()

    

    return render_template('influencersalesanalysis.html', celeb_data=celeb_data)


@views.route('/celebrity')
def celebrity():
    endpoint = '/service/celebrity/celebrity_id'
    api_url = f"{config['BASE_URL']}{endpoint}"

    celebrity_id = session.get('celebrity_id')
    print(celebrity_id)

    response = requests.post(api_url,json={"celebrity_id": celebrity_id})
    celeb_data = response.json()

    return render_template('celebrity.html', celeb_data=celeb_data)


@views.route('/api/extract-products', methods=['POST'])
def extract_products():
    try:
        # Get the magazine_id data from the request
        data = request.json

        endpoint = '/service/magazine/products'
        api_url = f"{config['BASE_URL']}{endpoint}"

        
        response = requests.post(api_url, json=data)
        

        if response.status_code == 200:
            return jsonify(response.json()), 200
        else:
            return jsonify({'error': 'Failed to extract products'}), 500

    except Exception as e:
        return jsonify({'error': str(e)}), 500 

