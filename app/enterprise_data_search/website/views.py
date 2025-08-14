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

#from flask_cors import CORS



config_file = os.getenv('CONFIG_FILE')
#config_file = 'website/config_dev.json'
print(f"The value of CONFIG_FILE is: {config_file}")



views = Blueprint('views', __name__)


@views.route('/', methods=['POST', 'GET'])
def styleme():
    
        return render_template('styleme.html')


@views.route('/stylemeqna', methods=['POST'])
def styleme_qna():
    # Get the magazine_id from the session
    conversation_list = []
    data = request.get_json()

    # Access the selected and question
    question = data.get('question')
    print(data)
    
    answer = ask_question_from_fashion(question)
        
    conversation_list.append({'User': question, 'Fashion Advisor': answer})
    #print(conversation_list)
    # Return the answer as a JSON response
    return jsonify({'answer': answer})



def ask_question_from_fashion(data):
    try:
        
        api_url = "https://dev-gen-ai-service-retail-kcvokjzgdq-ew.a.run.app/service/ai/bot"
        #api_url_stylemebot = 'https://dev-gen-ai-service-styleme-chat-kcvokjzgdq-ew.a.run.app/service/ai/stylemebot'
        payload = {
            'chat': data,
            
        }

        response = requests.post(api_url, json=payload)
        response.raise_for_status()  # Raise an exception for HTTP errors
        return response.json().get('answer', 'Sorry, I couldn\'t find an answer.')
    except requests.exceptions.RequestException as e:
        # Handle the exception and return an error response
        return 'An error occurred while communicating with the chatbot.'
