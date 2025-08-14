# Product Information Management

## Overview
The Product Information Management application is a Flask web service designed to extract specific information from a product description. It uses the Vertex AI Text Generation Model to generate prompts for extracting details such as product name, category, material, target segment, functional features, feature benefits, and product price.

## Installation
1. Install the required dependencies:
   ```bash
   pip install -r requirements.txt

2. Set up the Flask Application

```bash
export FLASK_APP=your_app_name.py
export FLASK_ENV=development
flask run

Replace your_app_name.py with the name of your Flask application file.

## API Endpoints

### 1. Product Information Management Page

- **Endpoint:** `/`
- **Method:** GET
- **Description:** Render the product information management page.
- **Response:** HTML page with the product information management interface.

### 2. Extract Information

- **Endpoint:** `/extract_info`
- **Method:** POST
- **Description:** Extract specific information from a product description.
- **Request Body:**
  ```json
  {
    "product_description": "Product description text..."
  }

### Response

```json
{
  "results": [
    "Extracted product name",
    "Extracted product category",
    "Extracted product material",
    "Extracted target segment",
    "Extracted functional features",
    "Extracted feature benefits",
    "Extracted product price"
  ]
}

## Model Initialization

The application initializes a TextGenerationModel from Vertex AI with the model name "text-bison@001". Adjust this as needed for your model.

## Example Usage

To extract product information, make a POST request to the `/extract_info` endpoint with the product description provided in the request body.

```vbnet
' Example code or additional information can be placed here
Note: Make sure to replace placeholders such as your_app_name.py with the actual names or values based on your application.