from flask import jsonify, request, render_template
from flask import Blueprint, render_template, url_for, request, session, redirect, Flask, jsonify, flash, make_response

from werkzeug.utils import secure_filename
import io
import json
import datetime
import hashlib
import random
import string



import requests
import re
import random
from flask_cors import CORS



import vertexai
from vertexai.language_models import TextGenerationModel
import json, datetime, time, requests

import os
from vertexai.preview.language_models import (TextGenerationModel)
import random






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




@views.route('/')
def sql_retail():
   

    return render_template('sql_retail.html')
 




model = TextGenerationModel.from_pretrained('text-bison@001')
max_output_tokens_val = 1000

# Function to call the OpenAI API with a prompt
def generate_sql(schema, data_quality_rules):
    prompt = f"Postgres SQL tables:\n\n{schema}\n\nCreate a SQL query to output the records that violate the following data quality rules:\n\n{data_quality_rules}\n\nSQL Code:\n"
    
    response = generation_model.predict(prompt=prompt, max_output_tokens=max_output_tokens_val, temperature= 0.1)
    full_text = response
    #print ("FULL TEXT >>>>>>>>>>> ", full_text)
        #sql_code, explanation = full_text.split('Explanation:', 1)
        #explanation = 'Explanation:' + explanation

    #return sql_code.strip(), explanation.strip()
    return response

# Define the input and output components
default_schema = '''#Product(id, name, category_id, brand_id, supplier_id, price, quantity, description, image, creation_date, discount, stock_threshold)
#Category(id, name, description)
#Brand(id, name, description)
#Supplier(id, name, email_id, contact_number, address, contract_start_date, contract_end_date)
#Store(id, name, address, city, zipcode, contact_number, email_id, opening_hours, manager_id)
#Employee(id, name, store_id, hire_date, job_title, contact, email_id, date_of_birth, address)
#Sales(id, transaction_id, store_id, employee_id, product_id, date, quantity, total_amount, payment_method)
#Inventory_Transaction(id, store_id, product_id, transaction_date, transaction_type, old_stock_level, new_stock_level, supplier_id)
#Customer(id, name, address, city, zipcode, contact_number, email_id, registration_date)
#Discounts(id, product_id, store_id, type, start_date, end_date, value)
#Sales_Return(id, transaction_id, store_id, product_id, date, quantity, reason)'''

@views.route('/service/ai/sql_retail', methods=['POST'])
def generate_sql():

    try:

        schema = request.json['previous_medical_record']
        data_quality_rules = request.json['latest_medical_record']
        prompt = f"Postgres SQL tables:\n\n{schema}\n\nCreate a SQL query to output the records that violate the following data quality rules:\n\n{data_quality_rules}\n\nSQL Code:\n"
        

        # Text generation parameters
        parameters = {
            "max_output_tokens": 1000,
            "temperature": 0.2,
            "top_p": 0.8,
            "top_k": 40
        }

        # Generate text using the model
        response = model.predict(prompt, **parameters)
        extracted_info = response.text

        return extracted_info

    except Exception as e:
        return jsonify({"error": str(e)})  
