import gradio as gr
import os

from vertexai.preview.language_models import (TextGenerationModel)
# os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'cdb-aia-ops-Palm.json'
generation_model = TextGenerationModel.from_pretrained('text-bison@001')
max_output_tokens_val = 1000

def extract_medical_info(report):
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

        response = generation_model.predict(prompt=prompt, max_output_tokens=max_output_tokens_val, temperature= 0.1)

        # Save the extracted information to the results list
        results.append(response)

    return tuple(results)

iface = gr.Interface(fn=extract_medical_info,
                     inputs=gr.Textbox(lines=10, label="Input the Product Description Text"),
                     outputs=[
                         gr.Textbox(label="1. Product Title/Name"),
                         gr.Textbox(label="2. Product Category"),
                         gr.Textbox(label="3. Product Material"),
                         gr.Textbox(label="4. Target Segment"),
                         gr.Textbox(label="5. Product Features"),
                         gr.Textbox(label="6. Feature Benefits"),
                         gr.Textbox(label="7. Price"),
                     ],
                     title="Product Information Management - Automated Metadata Extraction Tool",
                     description="Input a Product Description and the app will extract relevant information such as metadata elements corresponding to the product")

iface.launch(server_name="0.0.0.0", server_port=8080)
