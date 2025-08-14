# Claim Letter Page 

## Introduction
This README provides information about the "Claim Letter" page, along with the API service route used in the "gen-ai-service-retail" services.

## Description
The "Claim Letter" page serves as a tool for generating insurance claim letters. Users can input essential details, such as physician information, health insurance company details, patient information, and specific medical procedure and disease details. When users click the "Generate Letter" button, the system generates a letter in a predefined format, including all the necessary information for an insurance claim.

## API Service Route

### Base URL
- **Base URL**: [https://gen-ai-service-retail-kcvokjzgdq-ew.a.run.app]

### `/generate_claim_letter`
- **Description**: This route is used for generating insurance claim letters based on user-provided information.
- **Endpoint**: '/generate_claim_letter'
- **API URL**: [BASE_URL]/generate_claim_letter


### `/claimletter`
- **Description**: This view route displays the web page for creating and generating insurance claim letters.
- **Sample URL**: [Your_Application_URL]/claimletter

## Usage
To generate an insurance claim letter, access the "/claimletter" web page via your web browser. Enter the required details as described on the page, and click the "Generate Letter" button to obtain the claim letter.

If you need to programmatically generate a claim letter, you can use the `/generate_claim_letter` API route by sending the necessary data to the provided API URL.

## Conclusion
This README outlines the API service route and view route for the "Claim Letter" page. If you have any questions or need further assistance, please contact Akanksha Manro.