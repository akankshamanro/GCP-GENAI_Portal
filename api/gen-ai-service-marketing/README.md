# Customer Data Platform Analysis Service

This Flask application provides an API for analyzing Customer Data Platform (CDP) data using Vertex AI for text generation.

## Features

1. **Analyze CDP Data**: The `/analyze_cdp_data` endpoint takes customer data as input and generates insights based on predefined questions. It returns the results in JSON format.

2. **Service Health Check**: The `/service_marketing/health` endpoint provides a simple health check to verify the status of the service.

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
    The application will run on `http://0.0.0.0:8080/` by default.

## API Endpoints

### 1. Analyze CDP Data
- **Endpoint**: `/analyze_cdp_data`
- **Method**: POST
- **Request Body**:
    ```json
    {
        "cust_data": "Customer data in JSON format goes here."
    }
    ```
- **Response**:
    ```json
    {
        "1": "Customer Market Segment insights",
        "2": "Market Segment Justification insights",
        "3": "Personalized email insights",
        "4": "Banner Script insights"
    }
    ```

### 2. Service Health Check
- **Endpoint**: `/service_marketing/health`
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
- Use the provided API endpoint to analyze customer data and generate insights.

