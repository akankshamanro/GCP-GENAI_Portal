from flask import Flask, request, jsonify
from google.cloud import datastore
import vertexai
from vertexai.language_models import TextGenerationModel
import json, datetime, time, requests
from google.cloud import storage
import os
from flask_cors import CORS


app = Flask(__name__)
CORS(app)

# Initialize Vertex AI
vertexai.init(project=os.environ.get("PROJECT_ID"), VERTEX_REGION=os.environ.get("VERTEX_REGION"))

# Load the pre-trained text generation model
model = TextGenerationModel.from_pretrained("text-bison@001")
max_output_tokens_val = 1000

@app.route('/service_engineering', methods=['POST'])
def generate_answers():
    try:
        notes = request.json['notes']

        questions = [
            "What are the issues detected by each component type? answer in brief bullet points.",
            "What resolution actions were taken? answer in brief bullet points. Mention only those actions which have been performed upon equipments. Dont mention processes related to documentation etc",
            "How critical are the issues?answer in brief bullet points.",
            "What are the future recommendations for preventive maintenance?answer in brief bullet points. Mention only the recommendations mentioned in the notes.",
        ]

        answers = []

        for question in questions:
            prompt = f"{notes}\n\nQuestion: {question}\nAnswer:"
            response = model.predict(prompt=prompt, max_output_tokens=max_output_tokens_val, temperature=0.1)
            answers.append(response)

        return jsonify(answers)  # Return the answers as JSON

    except Exception as e:
        return jsonify({"error": str(e)}), 400
    
        
@app.route('/service_engineering/health', methods=['GET'])
def get_service_health():

    response = {
      "status": "healthy",     
      "status_code":200
                }
        
    return jsonify(response), 200


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)