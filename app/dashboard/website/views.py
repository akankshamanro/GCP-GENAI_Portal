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


views = Blueprint('views', __name__)
CORS(views) 

@views.route('/health', methods=['GET'])
def get_service_health():

    response = {
      "status": "healthy",     
      "app_name": "dashboard",     
      "status_code":200
                }
        
    return jsonify(response), 200

config_file = os.getenv('CONFIG_FILE')
print(f'config_file is {config_file}')


@views.route('/dashboard', methods = ['GET'])
def dashboard():
    print(config_file)
    return render_template("Dashboard.html",  config_file= config_file)





@views.route('/')
def home():
    return redirect('/dashboard')
