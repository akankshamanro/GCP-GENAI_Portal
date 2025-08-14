from flask import jsonify, request, render_template
from flask import Blueprint, render_template, url_for, request, session, redirect, Flask, jsonify, flash, make_response
import vertexai
import os
from vertexai.preview.language_models import (TextGenerationModel)
from flask import Flask, request, jsonify
from vertexai.language_models import TextGenerationModel
from flask_cors import CORS

app = Flask(__name__)
CORS(app)






views = Blueprint('views', __name__)
CORS(views)








@views.route('/')
def preventive_maintainance():
   

    return render_template('preventive_maintainance.html')
 





# Initialize Vertex AI
vertexai.init(project=os.environ.get("PROJECT_ID"), location=os.environ.get("VERTEX_REGION"))

# Load the pre-trained text generation model
model = TextGenerationModel.from_pretrained("text-bison@001")
max_output_tokens_val = 1000

def generate_answers(notes):
    questions = [
        "What are the issues detected by each component type? answer in brief bullet points.",
        "What resolution actions were taken? answer in brief bullet points. Mention only those actions which have been performed upon equipments. Dont mention processes related to documentation etc",
        "How critical are the issues?answer in brief bullet points.",
        "What are the future recommendations for preventive maintenance?answer in brief bullet points. Mention only the recommendations mentioned in the notes.",
    ]

    answers = []

    for question in questions:
        prompt = f"{notes}\n\nQuestion: {question}\nAnswer:"
        response = model.predict(prompt=prompt, max_output_tokens=max_output_tokens_val, temperature= 0.1)
        answers.append(response.text)

    return answers

@views.route('/generate_answers', methods=['POST'])
def api_generate_answers():
    try:
        # Get the JSON data from the request
        data = request.json

        # Call your extract_medical_info function with the provided data
        answers = generate_answers(data.get('medical_report', ''))

        # Create a JSON response
        response_data = {
            'answers': answers
        }

        return jsonify(response_data)
    except Exception as e:
        # Handle any errors or exceptions here
        return jsonify({'error': str(e)})
