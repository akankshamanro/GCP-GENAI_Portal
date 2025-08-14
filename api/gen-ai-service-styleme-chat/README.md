## StyleMeBot - Fashion AI Chat Service

StyleMeBot is a Flask-based application that provides an AI-powered fashion advice chat service. It utilizes Vertex AI for language models and offers personalized responses based on predefined user personas.

### Features

**Fashion Chat Advice**: The `/service/ai/stylemebot` endpoint engages in a chat conversation to provide fashion advice based on user input and a predefined persona.

### Getting Started

#### Prerequisites

- Python installed
- Install required Python packages using `pip install -r requirements.txt`
- Set environment variables:
  - `PROJECT_ID`: Your Google Cloud project ID
  - `VERTEX_REGION`: Vertex AI region

#### Run the Application

```bash
python app.py
The application will run on http://0.0.0.0:5000/ by default.

## Usage

### AI Fashion Chat Advice

- **Endpoint**: `/service/ai/stylemebot`
- **Method**: POST
- **Request Body**:

```json
{
    "chat": "user input text",
    "user_persona": "sample_persona"
}

## Response

```json
{
    "answer": "AI-generated response"
}

## User Personas

User personas, such as "sample_persona," are defined in a `persona.json` file. Ensure the file is correctly configured with the desired personas and their attributes.

## Model Initialization

The application initializes a ChatModel from Vertex AI with the model name "chat-bison@001". Adjust this as needed for your model.

## Examples

The application includes predefined examples for initiating the chat conversation. Modify or extend these examples to suit your application's context and requirements.
