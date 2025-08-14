from flask import Flask, request, jsonify
import vertexai
from vertexai.language_models import TextGenerationModel
import json, datetime, time, requests
import os
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Initialize Vertex AI
vertexai.init(project=os.environ.get("PROJECT_ID"), location=os.environ.get("VERTEX_REGION"))

# Load the pre-trained text generation model
model = TextGenerationModel.from_pretrained("text-bison@001")
max_output_tokens_val = 1000

def extract_product_info(report):

    info_to_extract = ["1. Product Name: What is the name of the product being described. Just provide the Product Name , do not start with 'The product name is'",
                    "2. Product Category: What is the name of the category of the product being described. Just provide the Product Category , do not start with 'The Product Category is'",
                    "3. Product Material: What is the material the product is made of?",
                    "4. Target Segment: Who is it the product's target segment?",
                    "5. Functional Features: What are the functional features of the product? List them.",
                    "6. Feature Benefits: Mention the benefits corresponding to each of the functional feature.",
                    "7. Product Price: Mention the price of the product. Respond as \'Price Not Provided\' in case its mot mentioned" 
                    ]

    results = []
    
    # Loop through the list of info_to_extract and send prompts to OpenAI API
    for info in info_to_extract:
        prompt = f"From the following Product Description, extract the {info}:\n{report}"

        response = model.predict(prompt=prompt, max_output_tokens=max_output_tokens_val, temperature= 0.1)

        # Save the extracted information to the results list
        results.append(response.text)

    return tuple(results)

@app.route('/extract_info', methods=['POST'])
def extract_info():
    try:
        # Get the JSON data from the request
        data = request.json

        # Call your extract_medical_info function with the provided data
        results = extract_product_info(data.get('report', ''))

        # Create a JSON response
        response_data = {
            'results': results
        }

        return jsonify(response_data)
    except Exception as e:
        # Handle any errors or exceptions here
        return jsonify({'error': str(e)})
    

@app.route('/service_management/health', methods=['GET'])
def get_service_health():

    response = {
      "status": "healthy",     
      "status_code":200
                }
        
    return jsonify(response), 200
    

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)    