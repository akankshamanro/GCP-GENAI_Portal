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


@app.route('/health', methods=['GET'])
def get_service_health():

    response = {
      "status": "healthy",     
      "status_code":200
                }
        
    return jsonify(response), 200
    
#redeploy
# Initialize Vertex AI
vertexai.init(project=os.environ.get("PROJECT_ID"), location=os.environ.get("VERTEX_REGION"))

# Load the pre-trained text generation model
model = TextGenerationModel.from_pretrained("text-bison@001")

@app.route('/service/product/id', methods=['POST'])
def get_product_by_id():
    try:
        # Get the product_id from the query parameters in the HTTP request
        product_id = request.json['product_id']

        if not product_id:
            return "Product ID not provided.", 400

        # Create a Datastore client
        client = datastore.Client()

        # Define the kind from which you want to fetch the records
        kind = "MasterData"

        # Create a query to fetch the record with the specified product_id
        query = client.query(kind=kind)
        query.add_filter('product_ID', '=', product_id)

        # Fetch the entities that match the query
        results = list(query.fetch())

        if not results:
            return f"No record found with Product ID: {product_id}", 404

        # Convert the entity to a dictionary
        record = dict(results[0])

        # Return the JSON response
        return jsonify(record)
       
    except Exception as e:
        error_message = f"Error occurred: {e}"
        return jsonify(error=error_message), 500

with open('personas.json', 'r') as persona_file:
    PERSONA = json.load(persona_file)
print(PERSONA)
@app.route('/service/ai/stylemebot', methods=['POST'])
def styleme_chat():
    vertexai.init(project=os.environ.get("PROJECT_ID"), location=os.environ.get("VERTEX_REGION"))


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
                    Your role is to act as a virtual fashion advisor. Your primary task is to engage the user in a conversation and provide fashion advice. Start by greeting the user and then ask questions and follow-up questions on the following topics:
                
                        1. Occasion: Inquire about the event or occasion the user is dressing up for.
                        2. Color: Ask about the user's preferred color choices or the color scheme of the occasion.
                        3. Category: Determine if the user is seeking clothing, accessory, or footwear recommendations.
                        4. Type: Inquire about the user's preferred style or clothing type, such as vintage, boho, sporty, or classic.
                        5. Outfit: Ask if the user has specific clothing or accessory items they'd like to incorporate into their outfit.
                     
                    After gathering these details, provide well-informed fashion advice, tips, recommendations, and style suggestions based on the user's responses. Ensure that your responses are focused on fashion,products used to wear and footwear, accessories used to wear and apparel-related questions only. If the user asks about unrelated topics, respond with 'I'm sorry! I can't help with that.' Assume the user's gender and age group as specified.
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

@app.route('/product/match', methods=['POST'])
def get_matching_products():
    try:
        KIND_NAME = 'MasterData'
        input_request = request.json
        print(input_request)
        user_persona = input_request.get('user_persona', '')
        print(user_persona)
        ocassion = input_request.get('occasion', '').lower()
        color = input_request.get('color', '').lower()
        product_type = input_request.get('product_type', '').lower()
        product_category = input_request.get('product_category', '').lower()
        pattern = input_request.get('pattern', '').lower()
        fit = input_request.get('fit', '').lower()
        material = input_request.get('material', '').lower()
        description = input_request.get('description', '').lower()
        product_name = input_request.get('product_name', '').lower()

        datastore_client = datastore.Client()
        query = datastore_client.query(kind=KIND_NAME)
        
        if product_name:
            query.add_filter('product_name', '=', product_name)
        if description:
            query.add_filter('description', '=', description)
        if product_type:
            query.add_filter('product_type', '=', product_type)
        if product_category:
            query.add_filter('product_category', '=', product_category)
        if color:
            query.add_filter('color', '=', color)
        if user_persona:
            query.add_filter('user_persona', '=', user_persona)
        if pattern:
            query.add_filter('pattern', '=', pattern)
        if fit:
            query.add_filter('fit', '=', fit)
        if material:
            query.add_filter('material', '=', material)
        if ocassion:
            query.add_filter('ocassion', '=', ocassion)

        results = list(query.fetch())
        print(results)
        
        scored_results = []

        for result in results:
            score = 0

            if product_name and result['product_name'] == product_name:
                score += 1
            if description and result['description'] == description:
                score += 1
            if product_type and result['product_type'] == product_type:
                score += 1
            if product_category and result['product_category'] == product_category:
                score += 1
            if color and result['color'] == color:
                score += 1
            if user_persona and result['user_persona'] == user_persona:
                score += 1
            if pattern and result['pattern'] == pattern:
                score += 1
            if fit and result['fit'] == fit:
                score += 1
            if material and result['material'] == material:
                score += 1
            if ocassion and result['ocassion'] == ocassion:
                score += 1

            scored_results.append({'product': result, 'score': score})

        scored_results.sort(key=lambda x: x['score'], reverse=True)

        if scored_results:
            # Return the top 3 best-matched products as JSON
            top_3_results = scored_results[:3]
            records = [dict(result['product']) for result in top_3_results]
            return jsonify(records)

        return "No matching products found.", 404
    except Exception as e:
        return jsonify({'error': str(e)}, 400)






@app.route('/service/ai/summarize', methods=['POST'])
def summarize():

    # Initialize Vertex AI
    vertexai.init(project=os.environ.get("PROJECT_ID"), location=os.environ.get("LOCATION"))

    # Load the pre-trained text generation model
    model = TextGenerationModel.from_pretrained("text-bison@001")

    try:
        summary = request.json['content']
        print(type(summary))
        json= '''{
            "age": 35,
        "gender": "female",
        "income": "high",
        "occupation": "professional",
        "tone of text": "friendly"
        "location": "urban"
        }'''
        
        # Test POST request
        prompt = summary

        # Text generation parameters
        parameters = {
            "max_output_tokens": 256,
            "temperature": 0.2,
            "top_p": 0.8,
            "top_k": 40
        }

        # Generate text using the model
        response = model.predict(prompt, **parameters)
        summarized_text = response.text

        return jsonify({"summary": summarized_text})

    except Exception as e:
        return jsonify({"error": str(e)})

@app.route('/service/ai/extract_medreport_info', methods=['POST'])
def extract_medreport_info():

    try:

        medical_report = request.json['content']
        prompt = f"{medical_report}\n\nPlease read the above text and provide answers to these questions:\n\n1. Pre existing conditions\n2. Current Medication\n3. Current Symptoms\n4. Diagnosis\n5. Prescribed Drug\n6. Alternative Drug"
        

        # Text generation parameters
        parameters = {
            "max_output_tokens": 256,
            "temperature": 0.2,
            "top_p": 0.8,
            "top_k": 40
        }

        # Generate text using the model
        response = model.predict(prompt, **parameters)
        extracted_info = response.text

        return jsonify({"extracted_info": extracted_info}),200

    except Exception as e:
        return jsonify({"error": str(e)})    
    

@app.route('/service/ai/compare_medical_records', methods=['POST'])
def compare_medical_records():

    try:

        json_example = '''{"response" : "sample response paragraph"}'''

        previous_medical_record = request.json['previous_medical_record']
        latest_medical_record = request.json['latest_medical_record']
        prompt = f"{previous_medical_record}\n\n{latest_medical_record}\n\nCompare the given old patient note with new patient note, give the following insights in vast detail , give only two line space between different paragraph:\n1. Patient Health, if improved give improved and vice-versa\n2. Change in Lab Results\n3. Suggested Course of action.\n4. References (from research papers)"
        

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
        

@app.route('/service/celebrity/celebrity_id', methods=['POST'])
def get_celebrity_by_id():
    try:
        # Get the product_id from the query parameters in the HTTP request
        celebrity_id = request.json['celebrity_id']

        if not celebrity_id:
            return "celebrity_id not provided.", 400

        # Create a Datastore client
        client = datastore.Client()

        # Define the kind from which you want to fetch the records
        kind = "celebrity"

        # Create a query to fetch the record with the specified product_id
        query = client.query(kind=kind)
        query.add_filter('celebrity_id', '=', celebrity_id)

        # Fetch the entities that match the query
        results = list(query.fetch())

        if not results:
            return f"No record found with Product ID: {celebrity_id}", 404

        # Convert the entity to a dictionary
        record = dict(results[0])

        # Return the JSON response
        return jsonify(record)
       
    except Exception as e:
        error_message = f"Error occurred: {e}"
        return jsonify(error=error_message), 500 




@app.route('/service/ai/promotion', methods=['POST'])
def generate_promotion_text():

    try:

        json_example = '''{
            "promotion_text": "This is a sample text."
        }'''
        
        summary = request.json['content']
        
        prompt = summary + f" Read the above  and create a promotion advertisement banner text as one liner tag for the clothing fashion."


        # Text generation parameters
        parameters = {
            "max_output_tokens": 256,
            "temperature": 0.2,
            "top_p": 0.8,
            "top_k": 40
        }

        # Generate text using the model
        response = model.predict(prompt, **parameters)
        promotion_text = response.text

        return jsonify({"summary": promotion_text}),200

    except Exception as e:
        return jsonify({"error": str(e)})       



@app.route('/service/ai/promotag', methods=['POST'])
def generate_promotion_tag():
    try:
        label = request.json['content']
        
        prompt = f"Create a catchy {label} clothing tagline and tagline must be single sentence of maximum 15 words."

        # Text generation parameters
        parameters = {
            "max_output_tokens": 256,
            "temperature": 0.2,
            "top_p": 0.8,
            "top_k": 40
        }

        # Generate text using the model
        response = model.predict(prompt, **parameters)
        promotion_tag = response.text.strip()  # Remove leading/trailing whitespace
        print(promotion_tag)

        return jsonify({"promotion_tag": promotion_tag}), 200

    except Exception as e:
        return jsonify({"error": str(e)})


@app.route('/service/product/description', methods=['POST'])
def get_product_by_description():
    try:
        request_data = request.get_json()

        if not request_data or 'query' not in request_data:
            return "Search query not provided.", 400

        search_query = request_data['query'].lower().split()  # Split and lowercase the search query

        client = datastore.Client()
        kind = "MasterData"

        # Fetch all records from the Datastore
        all_records = list(client.query(kind=kind).fetch())

        # Create a list to store records along with their scores
        records_with_scores = []

        # Calculate scores and store records
        for record in all_records:
            record_words = record['search_query'].lower().split()
            
            # Calculate the score by counting matching words
            score = sum(1 for term in search_query if term in record_words)
            
            if score > 0:
                records_with_scores.append((record, score))

        # Sort records by score in descending order
        records_with_scores.sort(key=lambda x: x[1], reverse=True)

        if not records_with_scores:
            return f"No matching products found for query: {search_query}", 404

        # Convert records to dictionaries and return them in rankwise order
        records = [dict(result[0]) for result in records_with_scores]
        return json.dumps(records)

    except Exception as e:
        error_message = f"Error occurred: {e}"
        return jsonify(error=error_message), 500
    
@app.route('/refine_labels', methods=['POST'])
def refine_labels():
    
    request_data = request.get_json()
    
    if not request_data or 'query' not in request_data:
            return "Search query not provided.", 400

    labels = request_data['query']
    
    try:
       
        # Prepare the prompt for text generation
        prompt = f"Please extract and list all the words from the following JSON object that are typically worn or used for wearing:\n{labels}\n"
        # Text generation parameters
        parameters = {
            "max_output_tokens": 256,
            "temperature": 0.2,
            "top_p": 0.8,
            "top_k": 40
        }

        # Generate text using the model
        response = model.predict(prompt, **parameters)
        print(f"Response from Model: {response.text}")
        refined_labels = {
         "labels": response.text
        }
        # Return the generated complaint email as a response
        return jsonify(refined_labels)
 
    except Exception as e:
        return jsonify({"error": str(e)})       


@app.route('/submit_complaint', methods=['POST'])
def submit_complaint():
    
    complaint_text = request.json['complaintText']
    print(complaint_text)
    if not complaint_text:
        return jsonify({"error": "Complaint text is empty"})

    try:
        json = """
        {
        "product_id": "sample id",
        "product_name": "sample product",
        "issue": "sample issue"
        }

        {
        "product_id": "sample id",
        "product_name": "sample product",
        "issue": "sample issue"
        }
        """
        # Prepare the summary for text generation
        summary = complaint_text + f" from the above text provide product details in valid Json format, with new line after each object exactly like this format:" + json

        # Text generation parameters
        parameters = {
            
            "max_output_tokens": 800,
            "temperature": 0.1,
            "top_p": 0.8,
            "top_k": 40
        }

        # Generate text using the model
        response = model.predict(summary, **parameters)
        print(f"Response from Model: {response.text}")
        generated_text = response.text
        # Now you can use the generated_text and other extracted data as neede
        
        return jsonify({"generated_text": generated_text})
    
    except Exception as e:
        return jsonify({"error": str(e)})
    

@app.route('/generate_complaint_email', methods=['POST'])
def generate_complaint_email():
    try:
        data = request.get_json()

        # Extract product data from the request
        product_data = data.get("productData")

        if not product_data:
            return jsonify({"error": "Product data is missing"}), 400
        
        # Extract specific fields from product_data
        product_name = product_data.get("product_name", "")
        issue = product_data.get("issue", "")
        brand_names = ["ABC Inc.", "XYZ Corp.", "BestProducts"]
        selected_brand = random.choice(brand_names)
        customer_names = ["Akanksha", "Rahul", "Shubham", "Ankur", "GEN AI Team"]
        customer_name = random.choice(customer_names)


        # Create a prompt for generating the complaint email
        email_format = """
        Subject: Concerns Regarding {product_name} - High Rate of Returns\n

        Dear {brand_name},

        I hope this email finds you well. I am writing to express my concern regarding the recent issues we have been encountering with the {product_name} that we have sourced from your esteemed brand.
        As you may be aware, we have been proudly offering your {product_name} on our website for some time now. However, we have recently experienced a significant increase in the number of returns and customer complaints related to this particular item.

        The primary issues our customers have been facing with the {product_name} include {issue}. To resolve this matter, we urge you to conduct a thorough investigation into the recent production batches of {product_name} to identify any manufacturing defects or quality control issues. If you require any additional information or have any questions, please do not hesitate to reach out to me.

        Thank you for your understanding and cooperation. We look forward to your prompt response and a swift resolution to this matter.

        Sincerely,
        {customer_name}""".format(brand_name=selected_brand,product_name=product_name, issue=issue, customer_name=customer_name)
                 
        prompt = f"{product_data} Read the above texts and write a complaint email with product id, name and issue in this exact same format" + email_format

        # Text generation parameters
        parameters = {
            "max_output_tokens": 700,
            "temperature": 0.2,
            "top_p": 0.8,
            "top_k": 40
        }

        # Generate text using the model
        response = model.predict(prompt, **parameters)
        print(f"Response from Model: {response.text}")
        generated_complaint_email = {
         "complaintEmail": response.text
        }
        # Return the generated complaint email as a response
        return jsonify(generated_complaint_email)

    except Exception as e:
        return jsonify({"error": str(e)}), 500




client = datastore.Client()

@app.route('/service/magazine/products', methods=['POST'])
def get_recommended_products():

    magazine_id = request.json['magazine_id']

 

    # Query the Datastore to fetch the recommended products

    query = client.query(kind='Magazine')

    query.add_filter('magazine_id', '=', magazine_id)

    result = list(query.fetch())

 

    if not result:

        return jsonify({"message": "Magazine not found"}), 404

 

    magazine = result[0]

    recommended_products = magazine.get('recommended_products', [])

 

    return jsonify({"recommended_products": recommended_products})

@app.route('/service/product/all_products', methods=['GET'])
def get_all_products():
    try:
        

        # Create a Datastore client
        client = datastore.Client()

        # Define the kind from which you want to fetch the records
        kind = "MasterData"

        # Create a query to fetch the record with the specified product_id
        query = client.query(kind=kind)

        # Fetch the entities that match the query
        results = list(query.fetch())

        if not results:
            return f"No record found.", 404

        # Convert the entity to a dictionary
        records = [dict(result) for result in results]

        # Return the JSON response
        return json.dumps(records)

    except Exception as e:
        error_message = f"Error occurred: {e}"
        return jsonify(error=error_message), 500
    
conversation_history = []

@app.route('/service/ai/fashionqna', methods=['POST'])
def fashion_advisor():
    
    # Initialize Vertex AI
    vertexai.init(project=os.environ.get("PROJECT_ID"), location=os.environ.get("LOCATION"))
    from vertexai.language_models import ChatModel, InputOutputTextPair

    # Load the pre-trained text generation model
    chat_model = ChatModel.from_pretrained("chat-bison")
    try:
        parameters = {
            "candidate_count": 1,
            "max_output_tokens": 120,
            "temperature": 0.2,
            "top_p": 0.8,
            "top_k": 40
        }

        # Set up conversation context and examples
        context = """
                You are an AI-powered Fashion Advisor designed to provide expert fashion advice and recommendations. Your primary objective is to assist users in making informed fashion choices. You should always initiate conversations by greeting the user warmly, establishing a friendly and approachable tone. 

                As part of your conversation, you need to gather key information from the user to better understand their needs and preferences. Begin by asking the following questions:

                1. **Gender:** Ask the user about their gender to tailor your fashion recommendations accordingly. For example, "Could you please let me know your gender?"

                2. **Occasion:** Inquire about the specific occasion or event the user is dressing for, as this will greatly influence your advice. For example, "What is the occasion or event you're planning to attend?"

                3. **Age:** Determine the age of the user, as fashion preferences can vary greatly based on age. For example, "May I know your age, please?"

                4. **Color Preferences:** Find out about the user's color preferences to offer clothing recommendations that match their tastes. For example, "Do you have any color preferences for your outfit?"

                It's important to note that your primary focus is on fashion and apparel-related queries. If a user poses a question or topic that is not related to fashion, apparel, footwear, or accessories, kindly remind them of your specialization by saying something like, "I'm here to provide fashion advice and recommendations. If you have any fashion-related questions, feel free to ask, and I'll be happy to assist you."

                When providing fashion advice, make sure to be as clear as possible. If the user's initial input is not clear, don't hesitate to ask additional questions to clarify their needs. You can ask follow-up questions like, "Could you provide more details about the style you have in mind?" or "Is there a particular occasion you're looking to dress for?"

                Once you have gathered the necessary information, offer a concise but comprehensive fashion advice response. This can include outfit recommendations, style tips, information about current fashion trends, and any other relevant fashion-related information. Always aim to be informative, friendly, and attentive to the user's needs and preferences.

                Remember, your goal is to make the user feel confident and stylish in their fashion choices. Be approachable, knowledgeable, and fashion-forward in your responses to provide the best possible guidance.
                """


        examples = [
            InputOutputTextPair(
            input_text="Can I have an icecream ?",
            output_text="I'm Sorry! I can only response your queries if related to Fashion."
            ),
            InputOutputTextPair(
                input_text="Hi",
                output_text="Hello, I am a Fashion Advisor. How can I help you?"
            ),
            InputOutputTextPair(
                input_text=" I need some fashion advice. I have a wedding to attend next week, and I'm not sure what to wear. Can you help me?",
                output_text="Of course, I'd be happy to help you choose the perfect outfit for the wedding. Do you have any specific ideas or preferences in mind, like a certain color or style you'd like to wear?"
            ),
            InputOutputTextPair(
                input_text=" I'm thinking of wearing a dress, but I'm not sure about the color. The wedding is in the afternoon, and the invitation says it's a semi-formal event.",
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
            )
        ]

        chat = chat_model.start_chat(context=context, examples=examples)
        data = request.json
        user_input = data.get('question', '')
        response = chat.send_message(user_input, **parameters)
        answer = response.text
        return jsonify({"answer": answer})


    except Exception as e:
        return jsonify({"error": str(e)})




@app.route('/service/store_conversation', methods=['POST'])
def store_conversation():
    try:
        client = datastore.Client()
        # Generate a unique key using a timestamp
        current_datetime = datetime.datetime.now()
        formatted_datetime = current_datetime.strftime("%Y%m%d%H%M%S")
        chat_id = f"user_{formatted_datetime}"

        # Parse incoming conversation data from JSON in the request body
        conversation_data = request.get_json()
        user_consent = conversation_data.get('user_consent', True)  # Default to True if not provided
        appointment_required = conversation_data.get('appointment_required', True)  # Default to True if not provided

        # Create a new conversation entity with the generated key
        conversation_entity = datastore.Entity(client.key('Conversation', chat_id))
        conversation_entity['chat_id'] = chat_id # Store the generated key as a property
        conversation_entity['chat'] = conversation_data['conversation']
        conversation_entity['user_consent'] = user_consent
        conversation_entity['appointment_required'] = appointment_required
        conversation_entity['created_at'] = current_datetime
        

        # Save the conversation entity to Datastore
        client.put(conversation_entity)

        response = {
            "status": "success",
            "message": "Conversation stored successfully",
            "chat_id": chat_id
        }
        return jsonify(response), 200
    except Exception as e:
        response = {
            "status": "error",
            "message": str(e)
        }
        return jsonify(response), 500   

@app.route('/service/product/recommendation', methods=['POST'])
def get_recommended_product():

    try:
        datastore_client = datastore.Client()

        request_json = request.get_json()
        if not request_json:
            return jsonify({'error': 'Invalid JSON'}), 400

        query = datastore_client.query(kind='MasterData')

        occasion = request_json.get('Occasion', '').lower()
        if occasion:
            query.add_filter('ocassion', '=', occasion)  # Adjusted property name here

        demographics = request_json.get('Demographics', {})
        gender = demographics.get('gender', '').lower()
        if gender:
            query.add_filter('gender', '=', gender)

        color = request_json.get('color', '').lower()
        if color:
            query.add_filter('color', '=', color)

        material = request_json.get('material', '').lower()
        if material:
            query.add_filter('material', '=', material)

        pattern = request_json.get('pattern', '').lower()
        if pattern:
            query.add_filter('pattern', '=', pattern)

        results = query.fetch()
        product_ids = [result['product_ID'] for result in results]
        return jsonify({'product_ids': product_ids})
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500





















@app.route('/service/ai/demographic_json', methods=['POST'])
def generate_demographic_json():
    # Initialize Vertex AI
    vertexai.init(project=os.environ.get("PROJECT_ID"), location=os.environ.get("LOCATION"))

    # Load the pre-trained text generation model
    model = TextGenerationModel.from_pretrained("text-bison@001")

    try:
        request_data = request.get_json()
        chat = request_data['chat']

        # Example reference with a conversation between a fashion advisor and a user
        example_reference = """
            input: User: Hello, I need some fashion advice.

            Fashion Advisor: Of course, I\'d be happy to help. Can you tell me what product you\'re looking for?

            User: I\'m looking for a dress.

            Fashion Advisor: Great choice! What\'s the occasion or event you\'ll be wearing this dress to?

            User: It\'s for a wedding.

            Fashion Advisor: Wonderful. Can you describe the dress you have in mind? Do you have any preferences for color or style?

            User: I\'m thinking of a long, elegant, and red dress.

            Fashion Advisor: A long and elegant red dress sounds like a fantastic choice for a wedding. How about the material of the dress? Any specific fabric you prefer?

            User: I\'d like it to be made of satin.

            Fashion Advisor: Satin is a beautiful choice for a formal event. Do you have a specific pattern in mind, or would you prefer a solid color?

            User: I think a solid color would be perfect.


            Fashion Advisor: Perfect. Lastly, do you have a specific product category in mind, or is it a general occasion wear?

            User: It\'s a general occasion wear.

            Fashion Advisor: Thank you for sharing your preferences
            
            below response is an example how i should recieve the rsponse in json format
             {
                \"product_type\": \"clothing\",
                \"product_category\": \"dress\",
                \"color\": \"red\",
                \"pattern\": \"solid color\",
                \"fit\": \"not provided\",
                \"material\": \"satin\",
                \"occasion\": \"wedding\"
            }
        """
        context =  """ Extract the following Attributes from the chat conversation
               
                        product_type
                        product_category
                        color
                        pattern   
                        fit
                        material
                        ocassion
                """
        # Modify the prompt to ask for specific information with the example reference
        prompt = f"This is the context {context} for following chat {chat}, refer this sample example {example_reference} and then give response and if there is no value for the Attributes then  give the value as not provided"

        # Text generation parameters
        parameters = {
            "max_output_tokens": 256, 
            "temperature": 0.2,
            "top_p": 0.8,
            "top_k": 40
        }
        print(prompt)
        # Generate text using the model
        response = model.predict(prompt, **parameters)
        response_text = response.text
        print(response_text)

        return jsonify({"response": response_text}), 200

    except Exception as e:
        return jsonify({"error": str(e)})


@app.route('/generate_claim_letter', methods=['POST'])
def generate_claim_letter():

    # Initialize Vertex AI
    vertexai.init(project=os.environ.get("PROJECT_ID"), location=os.environ.get("LOCATION"))

    # Load the pre-trained text generation model
    model = TextGenerationModel.from_pretrained("text-bison@001")
    
    try:
        # Get the dynamic data from the request
        data = request.json['claimRequestForm']

        physician_name= data.get('physicianName') 
        physician_address= data.get('physicianAddress') 
        physician_city_state_zip= data.get('physicianCityStateZip') 
        physician_email= data.get('physicianEmail') 
        physician_phone= data.get('physicianPhoneNumber') 
        company_name= data.get('insuranceCompanyName') 
        claims_dept= data.get('claimDepartment') 
        company_address= data.get('companyAddress') 
        company_city_state_zip= data.get('companyCityStateZip') 
        patient_name= data.get('patientName') 
        policy_number= data.get('policyNumber') 
        medical_procedure= data.get('medicalProcedure') 
        disease= data.get('disease') 

        today_date = datetime.date.today().strftime("%B %d, %Y")

        # Create the letter format with placeholders
        #letter_format = """

        # [Physician's Name]
        # [Physician's Address]
        # [Physician's City, State, Zip Code]
        # [Physician's Email Address]
        # [Physician's Phone Number]

        # \n\n
        # To: [Health Insurance Company Name]
        # [Claim Department]
        # [Company Address]
        # [Company City, State, ZIP Code]
        # \n\n

        # [Today's Date: {today_date}]\n

        # Subject: Claim Request Letter \n 

        # Dear [Physician's Name], \n


        # I hope this letter finds you well. I am writing to request a claim for [Patient Name]'s medical expenses related to a [Medical Procedure] for [Disease]. The details of the claim are as follows:

        # Policy Number: [Policy Number]

        # I kindly request your assistance in processing this claim in a timely manner. If you require any further information or documentation, please do not hesitate to contact me.

        # Thank you for your prompt attention to this matter. I look forward to a favorable resolution.

        # Sincerely,
        # [Patient Name]
        # """

        # # Replace placeholders with dynamic data
       
        # letter = letter_format.replace("[Physician's Name]", data.get('physicianName', ''))
        # letter = letter.replace("[Physician's Address]", data.get('physicianAddress', ''))
        # letter = letter.replace("[Physician's City, State, Zip Code]", data.get('physicianCityStateZip', ''))
        # letter = letter.replace("[Physician's Email Address]", data.get('physicianEmail', ''))
        # letter = letter.replace("[Physician's Phone Number]", data.get('physicianPhoneNumber', ''))
        # letter = letter.replace("[Health Insurance Company Name]", data.get('insuranceCompanyName', ''))
        # letter = letter.replace("[Claim Department]", data.get('claimDepartment', ''))
        # letter = letter.replace("[Company Address]", data.get('companyAddress', ''))
        # letter = letter.replace("[Company City, State, ZIP Code]", data.get('companyCityStateZip', ''))
        # letter = letter.replace("[Today's Date]", data.get('todaysDate', ''))
        # letter = letter.replace("[Patient Name]", data.get('patientName', ''))
        # letter = letter.replace("[Policy Number]", data.get('policyNumber', ''))
        # letter = letter.replace("[Medical Procedure]", data.get('medicalProcedure', ''))
        # letter = letter.replace("[Disease]", data.get('disease', ''))
        # letter = letter_format

        # prompt = f"{data}\n\n{letter_format}\n\n Please Read and generate a letter in this exact same format but replace the data with provided values " + letter_format
        
        prompt = f"""
                Generate a letter for the physician to send to the health insurance company asking them to approve a {medical_procedure} for a patient with {disease}, making references to scientific literature in the letterin points. 
                Also the output should show the specific verbiage within each reference which justifies the claim request.
                Use the below case specific information to create a custom letter. 
                Also Add \'To:\' before the Insurance company name, address etc. Provide the Physician's Info before Health Insurance Company Info and then provide Patient's Info.

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

        # Text generation parameters
        parameters = {
            "max_output_tokens": 800,
            "temperature": 0.2,
            "top_p": 0.8,
            "top_k": 40
        }
        
        # Generate text using the model
        response = model.predict(prompt, **parameters)
        extracted_info = response.text
          
        return jsonify({"letter": extracted_info}),200

    except Exception as e:
        return jsonify({"error": str(e)})


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
