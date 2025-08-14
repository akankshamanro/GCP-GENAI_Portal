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
      "app_name": "medical_comparision",
      "status_code":200
                }
        
    return jsonify(response), 200

storage_client = storage.Client()


@views.route('/')
def medicalComparision():
    selected_industry = 'pharma'

    # app_name = request.args.get('app_name')
    # team_members_info = get_team_members_by_app_name(app_name)

    # if team_members_info:
    #     for member in team_members_info:
    #         print(f"Name: {member['name']}, Role: {member['role']}")
    # else:
    #     print(f"No team members found for {app_name}")

    return render_template('medicalComparision.html', selected_industry= selected_industry)
 
