# Fashion AI Service

This Flask application provides various AI functionalities related to fashion, including product recommendations, chat-based fashion advice, text summarization, and more.

## Features

1. **Service Health Check**: The `/health` endpoint provides a simple health check to verify the status of the service.

2. **Product Recommendations**: The `/service/magazine/products` endpoint retrieves recommended products for a given magazine.

3. **Product Information by ID**: The `/service/product/id` endpoint retrieves detailed information about a product based on its ID.

4. **AI Chat for Fashion Advice**: The `/service/ai/stylemebot` endpoint engages in a chat conversation to provide fashion advice based on user input and a predefined persona.

5. **Generate Promotion Text**: The `/service/ai/promotion` endpoint generates promotional advertisement banner text based on input text.

6. **Generate Promotion Tag**: The `/service/ai/promotag` endpoint generates a catchy clothing tagline for promotional purposes.

7. **Summarize Text**: The `/service/ai/summarize` endpoint summarizes input text, useful for condensing large amounts of information.

8. **Extract Medical Report Information**: The `/service/ai/extract_medreport_info` endpoint extracts relevant information from medical reports.

9. **Compare Medical Records**: The `/service/ai/compare_medical_records` endpoint compares old and new medical records, providing insights into changes.

10. **Refine Labels**: The `/refine_labels` endpoint refines a list of words typically worn or used for wearing.

11. **Submit Complaint and Generate Email**: The `/submit_complaint` endpoint takes a complaint text, generates a product-related complaint email, and extracts product details in JSON format.

12. **Get All Products**: The `/service/product/all_products` endpoint retrieves all products from the Datastore.

13. **Fashion Q&A Chatbot**: The `/service/ai/fashionqna` endpoint provides a chat-based fashion question and answer service using a pre-trained model.

14. **Store Conversation**: The `/service/store_conversation` endpoint stores a chat conversation in the Datastore.

15. **Recommended Product based on Attributes**: The `/service/product/recommendation` endpoint retrieves recommended products based on user-specified attributes.

16. **Generate Demographic JSON**: The `/service/ai/demographic_json` endpoint generates JSON with demographic attributes based on a chat conversation.

17. **Generate Claim Letter**: The `/generate_claim_letter` endpoint generates a claim letter for medical expenses.

## Setup

1. **Prerequisites**:
    - Ensure you have Python installed.
    - Install required Python packages using `pip install -r requirements.txt`.
    
2. **Environment Variables**:
    - Set the necessary environment variables, including `PROJECT_ID`, `VERTEX_REGION`, `LOCATION`, and others as needed.

3. **Run the Application**:
    ```bash
    python app.py
    ```
    The application will run on `http://0.0.0.0:5000/` by default.

## API Endpoints

### 1. Service Health Check
- **Endpoint**: `/health`
- **Method**: GET
- **Response**:
    ```json
    {
        "status": "healthy",
        "status_code": 200
    }
    ```

### 2. Product Recommendations
- **Endpoint**: `/service/magazine/products`
- **Method**: POST
- **Request Body**:
    ```json
    {
        "magazine_id": "sample_magazine_id"
    }
    ```
- **Response**:
    ```json
    {
        "recommended_products": ["product_1", "product_2", "product_3"]
    }
    ```

### 3. Product Information by ID
- **Endpoint**: `/service/product/id`
- **Method**: POST
- **Request Body**:
    ```json
    {
        "product_id": "sample_product_id"
    }
    ```
- **Response**:
    ```json
    {
        "product_id": "sample_product_id",
        "product_name": "Sample Product",
        "description": "Product description",
        "price": "$99.99",
        "brand": "Sample Brand",
        "color": "Blue",
        "size": "Medium",
        "material": "Cotton",
        "user_persona": "Casual"
    }
    ```

### 4. AI Chat for Fashion Advice
- **Endpoint**: `/service/ai/stylemebot`
- **Method**: POST
- **Request Body**:
    ```json
    {
        "chat": "user input text",
        "user_persona": "sample_persona"
    }
    ```
- **Response**:
    ```json
    {
        "answer": "AI-generated response"
    }
    ```

### 5. Generate Promotion Text
- **Endpoint**: `/service/ai/promotion`
- **Method**: POST
- **Request Body**:
    ```json
    {
        "content": "input text for promotion generation"
    }
    ```
- **Response**:
    ```json
    {
        "summary": "Generated promotion text"
    }
    ```

### 6. Generate Promotion Tag
- **Endpoint**: `/service/ai/promotag`
- **Method**: POST
- **Request Body**:
    ```json
    {
        "content": "input label for promotion tag"
    }
    ```
- **Response**:
    ```json
    {
        "promotion_tag": "Generated promotion tag"
    }
    ```

### 7. Summarize Text
- **Endpoint**: `/service/ai/summarize`
- **Method**: POST
- **Request Body**:
    ```json
    {
        "content": "input text for summarization"
    }
    ```
- **Response**:
    ```json
    {
        "summary": "Generated summary"
    }
    ```

### 8. Extract Medical Report Information
- **Endpoint**: `/service/ai/extract_medreport_info`
- **Method**: POST
- **Request Body**:
    ```json
    {
        "content": "medical report text"
    }
    ```
- **Response**:
    ```json
    {
        "extracted_info": "Extracted information from the medical report"
    }
    ```

### 9. Compare Medical Records
- **Endpoint**: `/service/ai/compare_medical_records`
- **Method**: POST
- **Request Body**:
    ```json
    {
        "old_record": "text of old medical record",
        "new_record": "text of new medical record"
    }
    ```
- **Response**:
    ```json
    {
        "comparison_result": "Comparison result and insights"
    }
    ```

### 10. Refine Labels
- **Endpoint**: `/refine_labels`
- **Method**: POST
- **Request Body**:
    ```json
    {
        "labels": ["label1", "label2", "label3"]
    }
    ```
- **Response**:
    ```json
    {
        "refined_labels": ["refined_label1", "refined_label2", "refined_label3"]
    }
    ```

### 11. Submit Complaint and Generate Email
- **Endpoint**: `/submit_complaint`
- **Method**: POST
- **Request Body**:
    ```json
    {
        "complaint_text": "user's complaint text"
    }
    ```
- **Response**:
    ```json
    {
        "email": "Generated product-related complaint email",
        "product_details": {
            "product_id": "sample_product_id",
            "product_name": "Sample Product",
            "description": "Product description",
            "price": "$99.99",
            "brand": "Sample Brand",
            "color": "Blue",
            "size": "Medium",
            "material": "Cotton",
            "user_persona": "Casual"
        }
    }
    ```

### 12. Get All Products
- **Endpoint**: `/service/product/all_products`
- **Method**: GET
- **Response**:
    ```json
    [
        {
            "product_id": "product_1",
            "property1": "value1",
            "property2": "value2",
            ...
        },
        {
            "product_id": "product_2",
            "property1": "value1",
            "property2": "value2",
            ...
        },
        ...
    ]
    ```

### 13. Fashion Q&A Chatbot
- **Endpoint**: `/service/ai/fashionqna`
- **Method**: POST
- **Request Body**:
    ```json
    {
        "question": "user's fashion-related question"
    }
    ```
- **Response**:
    ```json
    {
        "answer": "AI-generated fashion advice"
    }
    ```

### 14. Store Conversation
- **Endpoint**: `/service/store_conversation`
- **Method**: POST
- **Request Body**:
    ```json
    {
        "conversation": "user's chat conversation",
        "user_consent": true,
        "appointment_required": true
    }
    ```
- **Response**:
    ```json
    {
        "status": "success",
        "message": "Conversation stored successfully",
        "chat_id": "generated_chat_id"
    }
    ```

### 15. Recommended Product based on Attributes
- **Endpoint**: `/service/product/recommendation`
- **Method**: POST
- **Request Body**:
    ```json
    {
        "Occasion": "wedding",
        "Demographics": {
            "gender": "female"
        },
        "color": "blue",
        "material": "silk",
        "pattern": "floral"
    }
    ```
- **Response**:
    ```json
    {
        "product_ids": ["product_1", "product_2", "product_3"]
    }
    ```

### 16. Generate Demographic JSON
- **Endpoint**: `/service/ai/demographic_json`
- **Method**: POST
- **Request Body**:
    ```json
    {
        "chat": "user's chat conversation"
    }
    ```
- **Response**:
    ```json
    {
        "response": "Generated demographic JSON based on chat conversation"
    }
    ```

### 17. Generate Claim Letter
- **Endpoint**: `/generate_claim_letter`
- **Method**: POST
- **Request Body**:
    ```json
    {
        "claimRequestForm": {
            "physicianName": "Dr. Smith",
            "physicianAddress": "123 Main St",
            "physicianCityStateZip": "City, State, ZIP",
            "physicianEmail": "dr.smith@example.com",
            "physicianPhoneNumber": "123-456-7890",
            "insuranceCompanyName": "ABC Insurance",
            "claimDepartment": "Claims Department",
            "companyAddress": "456 Company St",
            "companyCityStateZip": "Company City, State, ZIP",
            "patientName": "John Doe",
            "policyNumber": "ABC123",
            "medicalProcedure": "Surgery",
            "disease": "Chronic Condition"
        }
    }
    ```
- **Response**:
    ```json
    {
        "letter": "Generated claim letter for medical expenses"
    }
    ```

