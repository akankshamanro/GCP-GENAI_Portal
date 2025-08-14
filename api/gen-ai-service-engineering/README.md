# Service Engineering Flask App

This Flask application serves as a service engineering tool for generating answers to specific questions based on input notes. It utilizes the Vertex AI library and a pre-trained text generation model to provide insightful answers related to service engineering and preventive maintenance.

## Features

1. **Generate Answers**: The `/service_engineering` endpoint takes input notes and generates answers to predefined questions related to issues, resolution actions, issue criticality, and future recommendations.

2. **Service Health Check**: The `/service_engineering/health` endpoint provides a simple health check to verify the status of the service.

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

### 1. Generate Answers
- **Endpoint**: `/service_engineering`
- **Method**: POST
- **Request Body**:
    ```json
    {
        "notes": "Input notes for service engineering"
    }
    ```
- **Response**:
    ```json
    [
        "Answer to Question 1",
        "Answer to Question 2",
        "Answer to Question 3",
        "Answer to Question 4"
    ]
    ```

### 2. Service Health Check
- **Endpoint**: `/service_engineering/health`
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
- Use the provided API endpoints to interact with the service.
