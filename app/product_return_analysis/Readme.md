# Product Return Analysis Page 

## Introduction
This README provides information about the "Product Return Analysis" page and the API service routes used in the "gen-ai-service-retail" services.

## Description
The "Product Return Analysis" page is designed to manage customer complaints and generate email notifications to product manufacturers. It includes the following features:

- **Complaint Box Container**: Customers can submit complaints regarding the products they received.

- **Storage of Complaints**: Submitted complaints are stored in the product detail summary table, ensuring each complaint is documented.

- **Email Generation**: By clicking the "Generate Email" button, the system generates an email with essential information like the product ID, product name, and issue. This email is sent to the product manufacturer.

## API Service Routes

### Base URL
- **Base URL**: [https://gen-ai-service-retail-kcvokjzgdq-ew.a.run.app]

### `/submit_complaint`
- **Description**: This route is used for submitting customer complaints.
- **Endpoint**: '/submit_complaint'
- **API URL**: [BASE_URL]/submit_complaint

### `/generate_complaint_email`
- **Description**: This route is used to generate email notifications for submitted complaints.
- **Endpoint**: '/generate_complaint_email'
- **API URL**: [BASE_URL]/generate_complaint_email

### `/product_return_summary`
- **Description**: This route is used to retrieve product return data.
- **Endpoint**: '/product_return_summary'
- **API URL**: [BASE_URL]/product_return_summary
- **Request Parameters**:
 - product_id: The ID of the product for which you want to retrieve return data.
 - product_name: The name of the product.
 - issue: The issue associated with the returns.

## Usage
To interact with the API service routes, you can use HTTP clients such as cURL, Postman, or your preferred programming language. Use the provided API URLs and include the necessary request parameters.

## Conclusion
This README outlines the API service routes for the "Product Return Analysis" page and provides a brief description of the page's functionality. If you have any questions or need further assistance, please contact Akanksha Manro


