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
      "app_name": "product_catalog", 
      "status_code":200
                }
        
    return jsonify(response), 200

storage_client = storage.Client()
@views.route('/')
def productcatalog():
    

    return render_template('productcatalog.html')


@views.route('/api/send-labels', methods=['POST'])
def send_labels():
    try:
        # Get the labels data from the request
        data = request.json
        endpoint = '/service/product/description'
        api_url = f"{config['BASE_URL']}{endpoint}"

        #api_url_send_labels = 'https://gen-ai-service-retail-kcvokjzgdq-ew.a.run.app/service/product/description'
        response = requests.post(api_url, json=data)

        if response.status_code == 200:
            return jsonify(response.json()), 200
        else:
            return jsonify({'error': 'Failed to send data to external API'}), 500

    except Exception as e:
        return jsonify({'error': str(e)}), 500
    




@views.route('/product_tag', methods=['POST','GET'])
def product_tag():
    if request.method == 'POST':

        uploaded_image = request.files['file']
        if uploaded_image:
            # Ensure the filename is secure (prevents directory traversal attacks)
            filename = secure_filename(uploaded_image.filename)
            # Upload the image to GCS
            image_blob = upload_image_to_gcs(uploaded_image, filename)
            # Analyze the image using its GCS URI
            image_uri = f'gs://{config["bucket_name_image_upload"]}/{image_blob.name}'
            features = [vision.Feature.Type.LABEL_DETECTION,
                        vision.Feature.Type.OBJECT_LOCALIZATION,
                        vision.Feature.Type.SAFE_SEARCH_DETECTION,
                        vision.Feature.Type.IMAGE_PROPERTIES,
                        vision.Feature.Type.WEB_DETECTION
                        ]
            response = analyze_image_from_uri(image_uri, features)

            # Initialize an empty list to store all the results
            all_results = []

            # Extracting labels
            labels = [label.description.lower() for label in response.label_annotations]
            all_results.extend(labels)

            # Extracting object localizations
            object_localizations = [obj.name for obj in response.localized_object_annotations]
            all_results.extend(object_localizations)

                        
            #all_results.append(safe_search)

            face_detections = response.face_annotations
            for face in face_detections:
                all_results.append(face)  # You can modify the structure as needed

            # Extracting logo detection results
            logo_detections = [logo.description for logo in response.logo_annotations]
            all_results.extend(logo_detections)

            # Accessing the combined results
            print(all_results)

            data = {"query": all_results}
            
            endpoint = '/refine_labels'
            api_url = f"{config['BASE_URL']}{endpoint}"

            try:
                response_post = requests.post(api_url, json=data)
                response_post.raise_for_status()  # Raise an exception for non-200 status codes

                response_data = response_post.json()
                refined_labels = response_data.get("labels", "No labels available.")
                print(refined_labels)
                # Store the promotion result in the session
                
               
            except requests.exceptions.RequestException as e:
                print("POST Request Failed:", str(e))
                return jsonify({"error": "Failed to fetch promotion from the external API."}), 500


            # Combine clothing and color keywords into a single list
            all_keywords = clothing_keywords + color_keywords

            filtered_labels = [label for label in all_results if any(keyword in label for keyword in all_keywords)]
            clothing_labels = [label for label in all_results if any(keyword in label for keyword in clothing_keywords)]
            color_labels = [label for label in all_results if any(keyword in label for keyword in color_keywords)]

            if not filtered_labels:
                # If there are no filtered labels, render the message
                message = "Upload images which contain Apparels."
                session.clear()
                return render_template('productcatalog.html', message=message)
            elif not clothing_labels and color_labels:
                # If there are no clothing labels but there are color labels, render a different message
                message = "Upload images which contain Fashion objects."
                session.clear()
                return render_template('productcatalog.html', message=message)
            else:

                # Convert the filtered labels back to a space-separated string
                filtered_labels_text = ' '.join(filtered_labels)
                session['filtered_labels_text'] = filtered_labels_text

                # Create promotional text using the filtered labels
                template = "Make a two-line promotional advertisement text from {labels} for clothing and accessories!"
                #template = ""
                promotional_text = template.format(labels=filtered_labels_text)

                # Store the filtered promotional text in the session
                session['promotional_text'] = promotional_text

                # Render the template with the filtered labels
                return render_template('productcatalog.html', labels=filtered_labels)

    else:
        return render_template('productcatalog.html')
    
def upload_image_to_gcs(uploaded_image, filename):
    # Create a blob in the GCS bucket with the provided filename
    bucket = storage_client.bucket(config['bucket_name_image_upload'])
    image_blob = bucket.blob(filename)
    # Upload the image file to the blob
    image_blob.upload_from_string(uploaded_image.read(), content_type=uploaded_image.content_type)
    return image_blob


def analyze_image_from_uri(image_uri: str, feature_types: list) -> vision.AnnotateImageResponse:
    client = vision.ImageAnnotatorClient()
    image = vision.Image()
    image.source.image_uri = image_uri
    features = [vision.Feature(type_=feature_type) for feature_type in feature_types]
    request = vision.AnnotateImageRequest(image=image, features=features)

    response = client.annotate_image(request=request)
    print(response)
    return response
    
        

@views.route('/promotag')
def promotag():
    # Retrieve the first label from the session
    promotag = session.get('filtered_labels_text')
    
    if promotag is None:
        promotag = "Sorry, We couldn't identify a Fashion object in the image"
        #return jsonify({"error": "First label not found in session."}), 400
    
    data = {"content": promotag}
    
    endpoint = '/service/ai/promotag'
    api_url = f"{config['BASE_URL']}{endpoint}"

    try:
        response_post = requests.post(api_url, json=data)
        response_post.raise_for_status()  # Raise an exception for non-200 status codes

        response_data = response_post.json()
        promotion_tag = response_data.get("promotion_tag", "No promotion tag available.")
        print(promotion_tag)
        # Store the promotion result in the session
        
        return jsonify({"promotion_tag": promotion_tag})
    except requests.exceptions.RequestException as e:
        print("POST Request Failed:", str(e))
        return jsonify({"error": "Failed to fetch promotion from the external API."}), 500


@views.route('/promo')
def promo():
    # Retrieve the first label from the session
    promotional_text = session.get('promotional_text')
    print(promotional_text)
    
    if promotional_text is None:
        promotional_text = "Sorry, We couldn't identify a Fashion object in the image"
    

    
    data = {"content": promotional_text}
    
    endpoint = '/service/ai/promotion'
    api_url = f"{config['BASE_URL']}{endpoint}"

    response_post = requests.post(api_url, json=data)
    
    if response_post.status_code == 200:
        response_data = response_post.json()
        response = response_data.get("summary", "No summary available.")
        
        # Store the promotion result in the session
        session['promo'] = response
        
        return jsonify(response)
    else:
        print("POST Request Failed!")
        print(response_post.text)
        return jsonify({"error": "Failed to fetch promotion from the external API."}), 500



