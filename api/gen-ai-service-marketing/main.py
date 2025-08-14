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
vertexai.init(project=os.environ.get("PROJECT_ID"), location=os.environ.get("VERTEX_REGION"))

# Load the pre-trained text generation model
model = TextGenerationModel.from_pretrained("text-bison@001")

@app.route('/analyze_cdp_data', methods=['POST'])
def analyze_cdp_data():
    try:
        cust_data = request.json.get('cust_data')
        questions = [
            "1. Customer Market Segment - For the given CDP data for this customer, please suggest the Market Segment this customer belongs to. Give in bullet points only.",
            "2. Market Segment Justification - For the given CDP data for this customer, Pls provide 5 brief bullet points justification for this customer's market segment",
            "3. Personalized email - For the given CDP data for this customer, Pls create a personalized 15 line email for this customer which can be used to send as mail to this customer in the next campaign. Pls show only relevant categories relevant to the customer's behavior & interest. Dont show any coupon codes or offer percentages etc. Indicate to help in the area of interest",
            "4. Banner Script - For the given CDP data for this customer, Pls create an HTML-JavaScript code which can be used to show a personalized banner when the customer logs in next time. The banner should show the personalized categories of interest to the customer. The banner should not have basic info like age, gender, email id, etc. of the customer. DO NOT show the interaction history. DO NOT show the interaction details of the customer."
        ]

        results = {}  # Create a dictionary to store results in JSON format

      
        for i, question in enumerate(questions, 1):
            prompt = f"Customer Data Platform Data: {cust_data}\n\n{question}, return in valid JSON format"
            response = model.predict(prompt=prompt, temperature=0.1)
            results[f"{i}"] = response.text


        return jsonify(results)  # Return the results in JSON format

    except Exception as e:
        return jsonify({"error": str(e)})
    

@app.route('/service_marketing/health', methods=['GET'])
def get_service_health():

    response = {
      "status": "healthy",     
      "status_code":200
                }
        
    return jsonify(response), 200
    


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=int(os.environ.get('PORT', 8080)))