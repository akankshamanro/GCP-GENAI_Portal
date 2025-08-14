# Product Information Extraction Service

This Flask application provides an API for extracting specific information from product descriptions. It uses Vertex AI for text generation and model-based extraction.

## Features

1. **Extract Product Information**: The `/extract_info` endpoint takes a product description as input and extracts key information such as product name, category, material, target segment, functional features, feature benefits, and product price.

2. **Service Health Check**: The `/service_management/health` endpoint provides a simple health check to verify the status of the service.

## Setup

1. **Prerequisites**:
    - Ensure you have Python installed.
    - Install required Python packages using `pip install -r requirements.txt`.

2. **Environment Variables**:
    - Set the `PROJECT_ID` and `VERTEX_REGION` environment variables for Vertex AI integration.

3. **Run the Application**:
    ```bash
    python app.py
    ```
    The application will run on `http://0.0.0.0:5000/` by default.

## API Endpoints

### 1. Extract Product Information
- **Endpoint**: `/extract_info`
- **Method**: POST
- **Request Body**:
    ```json
    {
        "report": "Product description text goes here."
    }
    ```
- **Response**:
    ```json
    {
        "results": [
            "Extracted Product Name",
            "Extracted Product Category",
            "Extracted Product Material",
            "Extracted Target Segment",
            "Extracted Functional Features",
            "Extracted Feature Benefits",
            "Extracted Product Price"
        ]
    }
    ```

### 2. Service Health Check
- **Endpoint**: `/service_management/health`
- **Method**: GET
- **Response**:
    ```json
    {
        "status": "healthy",
        "status_code": 200
    }
    ```

## Notes
- Ensure the proper setup of the required environment variables.
- Use the provided API endpoint to extract information from product descriptions.

