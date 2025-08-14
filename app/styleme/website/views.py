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
#from flask_cors import CORS



config_file = os.getenv('CONFIG_FILE')

print(f"The value of CONFIG_FILE is: {config_file}")

with open(config_file) as f:
    config = json.load(f)



views = Blueprint('views', __name__)
#CORS(views)

@views.route('/health', methods=['GET'])
def get_service_health():

    response = {
      "status": "healthy",  
      "app_name": "styleme",   
      "status_code":200
                }
        
    return jsonify(response), 200

storage_client = storage.Client()



@views.route('/', methods=['POST', 'GET'])
def styleme():
    if request.method == 'POST':
        try:
            request_data = request.get_json()
            conversation_list = request_data.get('conversation')
            user_persona = request_data.get('persona')

            # Store the conversation in the datastore
            store_conversation_in_datastore({"conversation": conversation_list})

            # Prepare data for demographic analysis
            chat = convert_conversation_list_to_plain_text(conversation_list)
            data = {"chat": chat}
            demographic_endpoint = '/service/ai/demographic_json'
            demographic_api_url = f"{config['BASE_URL']}{demographic_endpoint}"

            # Make a request to the demographic analysis API
            demographic_response = requests.post(demographic_api_url, json=data)

            if demographic_response.status_code == 200:
                response_data = demographic_response.json()
                response_string = response_data.get('response')
                 
                if response_string is not None:
                    response_dict = json.loads(response_string)

                    # Filter out "not provided" values
                    filtered_response_dict = {key: value for key, value in response_dict.items() if value != "not provided"}
                    filtered_response_dict["user_persona"] = user_persona
                    print(f'filtered_response_dict:{filtered_response_dict}')
                    # Request product matching based on demographic analysis
                    product_matching_endpoint = '/product/match'
                    product_matching_api_url = f"{config['BASE_URL']}{product_matching_endpoint}"

                    response = requests.post(product_matching_api_url, json=filtered_response_dict)

                    if response.status_code == 200:
                        return jsonify(response.json()), 200
                    else:
                        return jsonify({'error': f"Request to /product/match failed with status code {response.status_code}"}), 500
                else:
                    return jsonify({'error': "The 'response' key was not found in the JSON response."}), 500
            else:
                return jsonify({'error': f"Request to the demographic API failed with status code {demographic_response.status_code}"}), 500
        except Exception as e:
            return jsonify({'error': str(e)}, 500)
    else:
        # Handle the GET request by fetching and rendering products
        products = fetch_products_styleme()
        return render_template('styleme.html', products=products)



'''@views.route('/', methods=['POST', 'GET'])
def styleme():
    if request.method == 'POST':
        try:
            request_data = request.get_json()
            print(request_data)
            conversation_list = request_data.get('conversation')
            chat = convert_conversation_list_to_plain_text(conversation_list)
            conversation = parse_conversation(chat)
            chat_conversation = {"conversation": conversation}
            
            response_message = store_conversation_in_datastore(chat_conversation)

            data = {"chat": chat}
            
            print(data)
            endpoint = '/service/ai/demographic_json'
            api_url = f"{BASE_URL}{endpoint}"
           
            response = requests.post(api_url, json=data)
            print(response)
            print(response.text)


            if response.status_code == 200:
                try:
                    # Parse the JSON response
                    response_data = response.json()
                    response_string = response_data.get('response')
                    print(response_string)

                    if response_string is not None:
                        # Decode the inner JSON
                        response_dict = json.loads(response_string)

                        # Create a new dictionary with non-"not provided" values
                        filtered_response_dict = {key: value for key, value in response_dict.items() if value != "not provided"}

                        # Print the filtered response
                        print(filtered_response_dict)

                        # You can return or use the filtered_response_dict as needed
                    else:
                        print("The 'response' key was not found in the JSON response.")
                except json.JSONDecodeError as e:
                    print("Failed to parse the JSON response from the API:", str(e))
            else:
                # Handle errors if the request was not successful
                print("Request failed with status code:", response.status_code)
                print("Error message:", response.text)



        except Exception as e:
            print("Error:", str(e))
        endpoint = '/service/product/description'
        api_url = f"{BASE_URL}{endpoint}" # Replace with the actual URL

        # Create a dictionary with the 'query' key and the response data
        request_data = {"query": " ".join(filtered_response_dict.values())}

        # Send a POST request to the API
        response = requests.post(api_url, json=request_data)
        print(response.json())

        if response.status_code == 200:
            # Process the response from the '/service/product/description' endpoint
            
            return jsonify(response.json()), 200
            
        
        else:
            # Handle errors if the request was not successful
            print("Request to /service/product/description failed with status code:", response.status_code)
            print("Error message:", response.text)

        # If any error occurs or no products are found, return an empty JSON
       

    else:
        
        products = fetch_products_styleme()
        return render_template('styleme.html', products=products)'''
    


def fetch_products_styleme():
    endpoint = '/service/product/all_products'
    api_url = f"{config['BASE_URL']}{endpoint}"
    response = requests.get(api_url)  # Replace with your actual API URL
    products = response.json()
    return products[:2]

@views.route('/stylemeqna', methods=['POST'])
def styleme_qna():
    # Get the magazine_id from the session
    conversation_list = []
    data = request.get_json()

    # Access the selected persona and question
    user_persona = data.get('persona')
    question = data.get('question')
    print(data)
    chat = convert_conversation_list_to_plain_text(conversation_list)
    
    
    answer = ask_question_from_fashion(question,user_persona)
        
    conversation_list.append({'User': question, 'Fashion Advisor': answer})
    #print(conversation_list)
    # Return the answer as a JSON response
    return jsonify({'answer': answer})


def convert_conversation_list_to_plain_text(conversation_list):
  """
  Converts a conversation list to plain text.

  Args:
    conversation_list: A list of conversation objects.

  Returns:
    A string of plain text representing the conversation.
  """

  plain_text = ""
  for conversation in conversation_list:
    plain_text += f"User: {conversation['User']}\n"
    plain_text += f"Fashion Advisor: {conversation['Fashion Advisor']}\n"
    print(plain_text)
  return plain_text



def ask_question_from_fashion(data,user_persona):
    try:
        
        #endpoint = '/service/ai/fashionqna'
        endpoint = '/service/ai/stylemebot'
        api_url = f"{config['api_url_stylemebot']}{endpoint}"
        #api_url_stylemebot = 'https://dev-gen-ai-service-styleme-chat-kcvokjzgdq-ew.a.run.app/service/ai/stylemebot'
        payload = {
            'chat': data,
            'user_persona': user_persona
            
        }

        response = requests.post(api_url, json=payload)
        response.raise_for_status()  # Raise an exception for HTTP errors
        return response.json().get('answer', 'Sorry, I couldn\'t find an answer.')
    except requests.exceptions.RequestException as e:
        # Handle the exception and return an error response
        return 'An error occurred while communicating with the chatbot.'
# Initialize an empty list to store the conversation
#conversation_list = []
def parse_conversation(text):
    lines = text.strip().split('\n')
    conversation = []
    sender = None
    current_message = []

    for line in lines:
        line = line.strip()
        if line.startswith('User:'):
            if sender and current_message:
                conversation.append({"sender": sender, "message": ' '.join(current_message)})
            sender = 'user'
            current_message = [line[len('User:'):].strip()]
        elif line.startswith('Fashion Assistant:'):
            if sender and current_message:
                conversation.append({"sender": sender, "message": ' '.join(current_message)})
            sender = 'bot'
            current_message = [line[len('Fashion Assistant:'):].strip()]
        else:
            current_message.append(line)

    if sender and current_message:
        conversation.append({"sender": sender, "message": ' '.join(current_message)})

    return conversation

# Function to take the JSON chat and store into datastore
def store_conversation_in_datastore(conversation_data):
    try:
        # Make a POST request to the cloud function
        endpoint = '/service/store_conversation'
        api_url = f"{config['BASE_URL']}{endpoint}"
        response = requests.post(api_url, json=conversation_data)

        if response.status_code == 200:
            response_data = response.json()  # Parse the response JSON
            chat_id = response_data.get("chat_id")  # Extract the entity key
            
            if chat_id:
                response_message = {
                    "message": "Conversation sent and stored successfully",
                    "chat_id": chat_id  # Include the entity key in the response
                }
                session['chat_id'] = chat_id
                print(session['chat_id'])
            else:
                response_message = {
                    "message": "Conversation sent and stored successfully"
                }
            
            return response_message
        else:
            return {
                "message": f"Error sending conversation: {response.text}"
            }
    except Exception as e:
        return {
            "message": str(e)
        }
    
