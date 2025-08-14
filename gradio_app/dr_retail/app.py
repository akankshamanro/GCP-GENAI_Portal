import gradio as gr
import os

from vertexai.preview.language_models import (TextGenerationModel)
# os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'cdb-aia-ops-Palm.json'
generation_model = TextGenerationModel.from_pretrained('text-bison@001')
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
schema_input = gr.Textbox(lines=6, label="Table Schema", default_schema)
rules_input = gr.Textbox(lines=6, label="Data Quality Rules")
output_sql = gr.Textbox(label="Data Quality SQL Code Gen")
#output_explanation = gr.Textbox(label="SQL Code Explanation")

# Create a Gradio interface and launch the app
iface = gr.Interface(fn=generate_sql, 
inputs=[schema_input, rules_input], outputs=[output_sql], title="Data Quality Check - SQL Generator App")

#iface.queue().launch(share=True)
iface.launch(server_name="0.0.0.0", server_port=8080) 
