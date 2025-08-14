# SQL Retail Service

This Flask application serves as a backend service for generating SQL queries related to retail data based on data quality rules. It utilizes OpenAI's Text Generation Model for this purpose.

## Endpoints

### 1. Health Check

- **Endpoint**: `/health`
- **Method**: `GET`
- **Description**: Check the health status of the service.
- **Response Example**:

```json
{
  "status": "healthy",
  "app_name": "medical_comparision",
  "status_code": 200
}

### 2. SQL Retail Generation

- **Endpoint**: /service/ai/sql_retail
- **Method**: POST
- **Description**: Generate SQL queries based on provided retail schema and data quality rules.
- **Response Example**:

```json
{
  "previous_medical_record": "<RETAIL_SCHEMA>",
  "latest_medical_record": "<DATA_QUALITY_RULES>"
}

### Response Example:

```json
{
  "generated_sql": "<GENERATED_SQL_QUERY>"
}

## Usage

Start the Flask application using the setup instructions.
Use the provided /service/ai/sql_retail endpoint with a POST request, providing the retail schema and data quality rules to generate SQL queries.

## Text Generation Model

The service utilizes OpenAI's Text Generation Model for SQL query generation. The model is loaded from the 'text-bison@001' pretrained version.

## Input Components

The default input schema and data quality rules are provided for testing purposes. Modify the default_schema and default_rules variables in the code as needed.

## Dependencies

Flask: Web framework for the backend
Flask-CORS: Enables CORS support for the Flask application
Vertex AI: Google Cloud's AI platform for machine learning models
Requests: HTTP library for making requests