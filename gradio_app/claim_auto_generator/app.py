import gradio as gr
import os
import datetime

from vertexai.preview.language_models import (TextGenerationModel)
# os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'cdb-aia-ops-Palm.json'
generation_model = TextGenerationModel.from_pretrained('text-bison@001')
max_output_tokens_val = 1000

def generate_letter(physician_name, physician_address, physician_city_state_zip, physician_email, 
                    physician_phone, company_name, claims_dept, company_address, 
                    company_city_state_zip, patient_name, policy_number, medical_procedure, disease):

    today_date = datetime.date.today().strftime("%B %d, %Y")

    # Define the prompt
    prompt = f"""
    Generate a letter for the physician to send to the health insurance company asking them to approve a {medical_procedure} for a patient with {disease}, making references to scientific literature. 
    Also the output should show within double quotes the specific verbiage within each reference which justifies the claim request.
    Use the below case specific information to create a custom letter.
    On the top of the letter, diplay the Tag name and the specific Tag values relaed to the Physician in the same row (dont show in different lines). 
    Start with the word \'To' before showing the Insurance company name, address etc. Display the Claims dept name before teh Health Ins company name. 

    Physician's Info:
    Physician's Name is {physician_name}
    Physician's Address is {physician_address}
    Physician's City, State, and ZIP is {physician_city_state_zip}
    Physician's Email Address is {physician_email}
    Physician's Phone Number is {physician_phone}
    Today's Date is {today_date}

    Health Insurance Company Info:
    Health Insurance Company Name is {company_name}
    Claims Department is {claims_dept}
    Company Address is {company_address}
    Company City, State, and ZIP is {company_city_state_zip}

    Patient's Info:
    Patient's Name is {patient_name}
    Policy Number is {policy_number}
    """

    response = generation_model.predict(prompt=prompt, max_output_tokens=max_output_tokens_val, temperature= 0.1)
    full_text = response
    #print ("FULL TEXT >>>>>>>>>>> ", full_text)
        #sql_code, explanation = full_text.split('Explanation:', 1)
        #explanation = 'Explanation:' + explanation

    #return sql_code.strip(), explanation.strip()
    return response

iface = gr.Interface(
    fn=generate_letter,
    inputs=[
        gr.Textbox("Dr. Jane Smith", lines=1, label="Physician's Name"),
        gr.Textbox("1234 Main St.", lines=1, label="Physician's Address"),
        gr.Textbox("Boston, MA, 02110", lines=1, label="Physician's City, State, ZIP"),
        gr.Textbox("jane.smith@example.com", lines=1, label="Physician's Email Address"),
        gr.Textbox("(555) 123-4567", lines=1, label="Physician's Phone Number"),
        gr.Textbox("XYZ Health Insurance", lines=1, label="Health Insurance Company Name"),
        gr.Textbox("Medical Claims Department", lines=1, label="Claims Department"),
        gr.Textbox("5678 Elm St.", lines=1, label="Company Address"),
        gr.Textbox("Boston, MA, 02111", lines=1, label="Company City, State, ZIP"),
        gr.Textbox("John Doe", lines=1, label="Patient's Name"),
        gr.Textbox("ABC123456", lines=1, label="Policy Number"),
        gr.Textbox(lines=1, label="Medical Procedure"),
        gr.Textbox(lines=1, label="Disease"),
    ],
    outputs=gr.Textbox(label="Generated Letter"),
    title="Claim Request Letter Generator",
    description="Generate a letter to a health insurance company requesting approval for a specific medical procedure for a patient with a particular disease, making references to scientific literature.",
)



#iface.queue().launch(share=True)
iface.launch(server_name="0.0.0.0", server_port=8080)
