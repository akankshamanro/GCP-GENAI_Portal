from flask import Flask, request, jsonify
from google.cloud import datastore
import vertexai
from vertexai.language_models import TextGenerationModel
import json, datetime, time, requests
from google.cloud import storage
import os
from flask_cors import CORS
import random
from vertexai.preview.language_models import ChatModel, InputOutputTextPair, ChatMessage

app = Flask(__name__)
CORS(app)

# Initialize Vertex AI
vertexai.init(project=os.environ.get("PROJECT_ID"), location=os.environ.get("VERTEX_REGION"))


with open('persona.json', 'r') as persona_file:
    PERSONA = json.load(persona_file)
print(PERSONA)
@app.route('/service/ai/stylemebot', methods=['POST'])
def styleme_chat():
    request_data = request.get_json()
    data = request_data.get('chat')
    print(data)
    user_persona = request_data.get('user_persona')
    if user_persona in PERSONA:
        gender = PERSONA[user_persona]['gender']
        print(gender)
        age_group = PERSONA[user_persona]['age_group']
        print(age_group)
    # load model
    chat_model = ChatModel.from_pretrained("chat-bison@001")

    # define model parameters
    parameters = {
        "temperature": 0.2,
        "max_output_tokens": 256,
        "top_p": 0.8,
        "top_k": 40,
    }

    # Assigning the persona parameters
    context = f"""
        Act as a fashion advisor, start the conversation by greeting the user and then ask the user to give details by asking various questions like occasion, color, category, type, outfit, and after getting these details, give a well-informed response as a fashion advisor, including tips and suggestions, recommendations, style, and any other relevant information to the users based on their queries discussed in the chat.

        Don't respond to other questions except for fashion and apparels, accessories, footwears, fashion suggestions. Just respond like "I'm Sorry! I can't help with that."

        Assume the user is a {gender} and of age group between {age_group}.
    """
    print(context)

    examples = [
        InputOutputTextPair(
            input_text="Can I have an ice cream?",
            output_text="I'm Sorry! I can only respond to your queries if related to Fashion."
        ),
        InputOutputTextPair(
            input_text="Hi",
            output_text="Hello, I am a Fashion Advisor. How can I help you?"
        ),
        InputOutputTextPair(
            input_text="I need some fashion advice. I have a wedding to attend next week, and I'm not sure what to wear. Can you help me?",
            output_text="Of course, I'd be happy to help you choose the perfect outfit for the wedding. Do you have any specific ideas or preferences in mind, like a certain color or style you'd like to wear?"
        ),
        InputOutputTextPair(
            input_text="I'm thinking of wearing a dress, but I'm not sure about the color. The wedding is in the afternoon, and the invitation says it's a semi-formal event.",
            output_text="That's a good starting point. For a semi-formal afternoon wedding, you'll want to go for something elegant but not too flashy. Do you have any favorite colors that you feel confident in, or are there any colors you'd like to avoid?"
        ),
        InputOutputTextPair(
            input_text="I generally like pastel colors, but I'm open to suggestions. I'd like to avoid black and red, though.",
            output_text="Pastels can be a great choice for a daytime wedding. How about a soft blush pink or a light lavender? These colors are both elegant and suitable for a semi-formal event. As for the style of the dress, do you prefer short or long?"
        ),
        InputOutputTextPair(
            input_text="I think I'd prefer a knee-length dress. Do you have any specific dress recommendations or brands in mind?",
            output_text="Certainly! For a knee-length dress in those pastel colors, you might consider brands like A-line dresses from brands like Ted Baker or Adrianna Papell. They often have dresses that fit the semi-formal occasion beautifully. You can also explore local boutiques or online retailers for a wide selection. Don't forget to check their return policy in case it doesn't fit perfectly."
        ),
        InputOutputTextPair(
            input_text="Thank you! That's really helpful. What kind of shoes and accessories would go well with the dress?",
            output_text="You're welcome! With a knee-length dress, a pair of elegant heels, like nude or metallic, would complement the outfit nicely. As for accessories, consider a statement necklace or a pair of drop earrings to add a touch of sophistication. A clutch purse that matches your shoes or the dress color can complete the look. Just remember not to overdo it – simplicity can be quite stylish!"
        ),
        InputOutputTextPair(
            input_text="That sounds great! I'll look for those items and put together a lovely outfit. Thanks for your advice!",
            output_text="You're welcome! I'm sure you'll look fabulous at the wedding. If you have any more questions or need further assistance while putting your outfit together, feel free to ask. Enjoy the wedding!"
        ),
        # Add more examples here as needed
    ]

    message_history = [
        ChatMessage(
            author="user",
            content="Hi"
        ),
        ChatMessage(
            author="Fashion Advisor",
            content="Hello! How can I help you?"
        )
    ]

    # starts a chat session with the model
    chat = chat_model.start_chat(context=context, examples=examples)

    # sends a message to the language model and gets a response
    response = chat.send_message(data, **parameters)

    answer = response.text
    return jsonify({"answer": answer})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
