import gradio as gr

import os

from vertexai.preview.language_models import (TextGenerationModel)
# os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'cdb-aia-ops-Palm.json'
generation_model = TextGenerationModel.from_pretrained('text-bison@001')
max_output_tokens_val = 1000

def analyze_claim_letter(input_letter):
    info_to_extract = [
        "1) Decide if this case mentioned in the letter should be 'Recommended for approval' or 'Staged for Scrutiny'. Just provide the decision. Dont explain."  ,
        "2) Explain the Reasons why this case mentioned in the letter should be approved or rejected (if its to be Approved then only show the reasons for approval. Similarly, id the claim is to be Rejected then show only the reasons for Rejection). Justify. Lets think step by step."
    ]

    results = []

    for info in info_to_extract:
        prompt = f"Given below in triple backticks is a letter from a Physician seeking Claim approval for a medical procedure. thinking as a health insurance company's claim adjudicator, please guide on the case: \n{info}\n```\n{input_letter}\n```"

        response = generation_model.predict(prompt=prompt, max_output_tokens=max_output_tokens_val, temperature= 0.1)

        results.append(response)

    return tuple(results)

iface = gr.Interface(
    fn=analyze_claim_letter,
    inputs=gr.Textbox(lines=20, label="Enter the claim letter"),
    outputs=[
        gr.Textbox(label="Decision"),
        gr.Textbox(label="Justification"),
    ],
    title="Medical Claim Adjudication Assistant",
    description="Get guidance on medical claim adjudication using GPT",
)

#iface.queue().launch(share=True)
iface.launch(server_name="0.0.0.0", server_port=8080)
