import gradio as gr
import os

from vertexai.preview.language_models import (TextGenerationModel)
# os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'cdb-aia-ops-Palm.json'
generation_model = TextGenerationModel.from_pretrained('text-bison@001')
max_output_tokens_val = 1000

def generate_answers(notes):
    questions = [
        "What are the issues detected by each component type? answer in brief bullet points.",
        "What resolution actions were taken? answer in brief bullet points. Mention only those actions which have been performed upon equipments. Dont mention processes related to documentation etc",
        "How critical are the issues?answer in brief bullet points.",
        "What are the future recommendations for preventive maintenance?answer in brief bullet points. Mention only the recommendations mentioned in the notes.",
    ]

    answers = []

    for question in questions:
        prompt = f"{notes}\n\nQuestion: {question}\nAnswer:"
        response = generation_model.predict(prompt=prompt, max_output_tokens=max_output_tokens_val, temperature= 0.1)
        answers.append(response)

    return answers

iface = gr.Interface(
    fn=generate_answers,
    inputs=gr.Textbox(lines=10, label="Maintenance Engineer's Notes"),
    outputs=[
        gr.Textbox(label=q) for q in [
            "Issues Detected",
            "Resolution Actions",
            "Criticality",
            "Preventive Maintenance Recommendations",
        ]
    ],
    title="Preventive Maintenance - Inspection Engineer Notes Analysis",
)

#iface.queue().launch(share=True)
iface.launch(server_name="0.0.0.0", server_port=8080)
