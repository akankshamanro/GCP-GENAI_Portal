import gradio as gr
import os

from vertexai.preview.language_models import (TextGenerationModel)
# os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'cdb-aia-ops-Palm.json'
generation_model = TextGenerationModel.from_pretrained('text-bison@001')
max_output_tokens_val = 1000

def analyze_cdp_data(cust_data):
    
    questions = [
        "1. Customer Market Segment - For the given CDP data for this customer, please suggest the Market Segment this customer belongs to. Give in bullet points only.",
        "2. Market Segment Justification - For the given CDP data for this customer, Pls provide 5 brief bullet points justification for this customer's market segment",
        "3. Personalized email - For the given CDP data for this customer, Pls create a personalized 15 line email for this cusomer which can be used to send as mail to this customer in the next campaign. Pls show only relevant categories relevant to the customer's behavior & interest. dont show any coupon codes or offer percentages etc. Indicate to help in the area of interest",
        "4. Banner Script - For the given CDP data for this customer, Pls create a html-javascript code which can be used to show a personalized banner when the customer logs in next time. The benner should show the personalized categories of interest to the customer. The banner should not have basic info like age, gender, email id, etc of the customer. DO NOT show the interaction history . SO NOT show the interaction details of the customer."
    ]

    results = []

    for question in questions:
        prompt = f"Customer Data Platform Data: {cust_data}\n\n{question}"
        response = generation_model.predict(prompt=prompt, max_output_tokens=max_output_tokens_val, temperature= 0.1)
        results.append(response)
    return results

def gradio_wrapper(cdp_data):
    results = analyze_cdp_data(cdp_data)
    return [result for i, result in enumerate(results)]

iface = gr.Interface(
    fn=gradio_wrapper,
    inputs=gr.Textbox(lines=10, placeholder="Enter CDP data here......"),
    outputs=[
        gr.Textbox(label="Customer Market Segment"),
        gr.Textbox(label="Market Segment Justification"),
        gr.Textbox(label="Personalized Email"),
        gr.Textbox(label="Website Personalized Banner Script")
    ],
    title="Customer Data driven Personalized Marketing App",
    description="Analysis of Customer Data Platform to generate Personalized Marketing Messages",
)
#iface.queue().launch(share=True)
iface.launch(server_name="0.0.0.0", server_port=8080)
