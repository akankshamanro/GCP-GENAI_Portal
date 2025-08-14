import gradio as gr
import os

from vertexai.preview.language_models import (TextGenerationModel)
# os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'cdb-aia-ops-Palm.json'
generation_model = TextGenerationModel.from_pretrained('text-bison@001')
max_output_tokens_val = 1000


# Function to call the OpenAI API with a prompt
def generate_sql(schema, data_quality_rules):
    prompt = f"Postgres SQL tables:\n\n{schema}\n\nCreate a SQL query to output the records that violate the data quality rules:\n\n{data_quality_rules}\n\nSQL Code:\n"
    
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
schema_input = gr.Textbox(default_schema,lines=6, label="Table Schema")
rules_input = gr.Textbox(default_rules,lines=6, label="Data Quality Rules")
output_sql = gr.Textbox(label="Data Quality SQL Code Gen")


# Create a Gradio interface and launch the app
iface = gr.Interface(fn=generate_sql, inputs=[schema_input, rules_input], outputs=[output_sql], title="Data Quality SQL Generator")

#iface.queue().launch(share=True)
iface.launch(server_name="0.0.0.0", server_port=8080)