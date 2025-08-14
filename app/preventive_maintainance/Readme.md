# Preventive Maintenance Application

This Flask application serves as a preventive maintenance tool that generates answers based on given medical reports.

## Getting Started

### Prerequisites

Make sure you have the required dependencies installed:

```bash
pip install Flask vertexai

## Setup

1. **Clone the repository:**

   ```bash
   git clone <repository-url>
   cd <repository-directory>


2. Set up your environment variables:

```bash
export PROJECT_ID=<your-project-id>
export VERTEX_REGION=<your-vertex-region>

3. Running the Application

Run the Flask application:

```bash
flask run

## API Endpoints

### Generate Answers

- **Endpoint:** /generate_answers
- **Method:** POST

**Response Example:**

```json
{
  "medical_report": "<medical-report-text>"
}

## Response Example

```json
{
  "answers": [
    "Answer to question 1",
    "Answer to question 2",
    "Answer to question 3",
    "Answer to question 4"
  ]
}

## Usage

1. Access the application at [http://localhost:5000/](http://localhost:5000/).
2. Use the `/generate_answers` endpoint with a POST request, providing the medical report text to generate answers.

## Implementation Details

- The application utilizes the Vertex AI platform for the text generation model.
- The model is loaded from the 'text-bison@001' pretrained version.
- The frontend is implemented using Flask and renders the 'preventive_maintainance.html' template.

## Dependencies

- Flask: Web framework for the backend
- vertexai: Vertex AI library for machine learning models

```javascript
// Note: Replace `<repository-url>`, `<repository-directory>`, `<your-project-id>`, `<your-vertex-region>`, and `<medical-report-text>` with your actual values. Adjust the formatting and content as needed for your specific documentation.
