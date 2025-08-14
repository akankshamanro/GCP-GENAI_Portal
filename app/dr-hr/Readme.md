# SQL-HR Service

## Introduction

This Flask application serves as a backend service for generating SQL queries related to HR data based on data quality rules. It utilizes OpenAI's Text Generation Model for this purpose.

## Setup

1. Install dependencies:

   ```bash
   pip install Flask flask_cors vertex-ai requests

## Setup Instructions

### Clone the Repository

```bash
git clone <repository-url>
cd <repository-directory>

### Run the Flask Application

```bash
flask run

## Endpoints

### 1. Health Check

- **Endpoint**: `/health`
- **Method**: `GET`
- **Description**: Check the health status of the service.
- **Response Example**:

### Request Example 

```json
{
  "status": "healthy",
  "app_name": "medical_comparision",
  "status_code": 200
}

### 2. SQL-HR Generation

- **Endpoint**: `/service/ai/sql_hr`
- **Method**: `POST`
- **Description**: Generate SQL queries based on provided HR schema and data quality rules.
  
### Request Example

```json
{
  "previous_medical_record": "<HR_SCHEMA>",
  "latest_medical_record": "<DATA_QUALITY_RULES>"
}
```json
{
  "generated_sql": "<GENERATED_SQL_QUERY>"
}

## Usage

1. Start the Flask application using the setup instructions.
2. Use the provided `/service/ai/sql_hr` endpoint with a POST request, providing the HR schema and data quality rules to generate SQL queries.

## Text Generation Model

The service utilizes OpenAI's Text Generation Model for SQL query generation. The model is loaded from the 'text-bison@001' pretrained version.

## Input Components

The default input schema and data quality rules are provided for testing purposes. Modify the `default_schema` and `default_rules` variables in the code as needed.

## Dependencies

- Flask: Web framework for the backend
- Flask-CORS: Enables CORS support for the Flask application
- Vertex AI: Google Cloud's AI platform for machine learning models
- Requests: HTTP library for making requests
