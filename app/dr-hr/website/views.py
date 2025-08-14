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
def sql_hr():
   

    return render_template('sql_hr.html')
 




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
default_schema = '''#Employee(id, name, department_id, hire_date, job_title, salary, bonus, experience, date_of_birth, email_id, address)
#Department(id, name, address, founded, company_type, total_employees, annual_revenue, industry_sector)
#Salary_Payments(id, employee_id, amount, date, payment_reference, payment_method, deduction_amount, bonus_amount)
#Contracts(id, employee_id, start_date, end_date, job_title, salary)
#Time_Sheets(id, employee_id, day, hours_worked)'''

default_rules = '''RULE: All employees who have been employed within the last 90 days should have a contract

RULE: All employees who have worked more than 7 hours per day in the last 2 weeks should have a salary payment

RULE: All salary payments should be recorded in ISO 8601 date format (yyyy-mm-dd)

RULE: Employees in the same department with the same job title must have consistent salary ranges with a maximum difference of 5000 if they have the same experience level.

RULE: Employees should have consistent job titles, salary ranges, and experience levels per department, and no salary payment should be overdue by more than 15 days
'''

@views.route('/service/ai/sql_hr', methods=['POST'])
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
