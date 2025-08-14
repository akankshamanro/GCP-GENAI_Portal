# Medical Comparison Page

## Introduction
This README provides information about the "Medical Comparison" page, a tool for comparing recent and previous medical reports to extract key insights about diseases, provide references, and suggest measures to be taken.

## Description
The "Medical Comparison" page facilitates the comparison of recent and previous medical reports, enabling users to gain valuable insights about the patient's health. It also helps in identifying changes in lab results, suggesting courses of action, and offering references to relevant research papers. Key features include:

- **Report Comparison**: Users can input both recent and previous medical reports for comprehensive analysis.

- **Insight Extraction**: The tool extracts insights about the patient's health, changes in lab results, and provides recommendations for a course of action.

- **References**: References to relevant research papers are included for further reading and reference.

- **Measures to Be Taken**: The tool suggests practical measures or actions to address the patient's condition.

## API Service Routes

### `/service/ai/compare_medical_records`
- **Description**: This route handles the comparison of recent and previous medical records and provides insights, references, and suggested measures.
- **Endpoint**: '/service/ai/compare_medical_records'
- **Method**: POST
- **Sample JSON Data**:
  ```json
  {
    "previous_medical_record": "Previous medical report text",
    "latest_medical_record": "Recent medical report text"
  }

## Output: 
The API response contains extracted insights and information.

## View Route
### /medicalComparison

**Description**: This view route displays the "Medical Comparison" page, where users can input recent and previous medical reports for comparison.
**Sample URL**: [https://dev-gen-ai-service-retail-kcvokjzgdq-ew.a.run.app]/medicalComparison

## Usage
Access the "Medical Comparison" page on your web browser.
Input the recent and previous medical reports for comparison.
Click the "Compare" button to obtain insights, references, and suggested measures based on the comparison.

## Conclusion
This README outlines the "Medical Comparison" page's functionality for comparing medical reports, extracting insights, providing references, and suggesting measures to be taken. If you have any questions or need further assistance, please contact Rahul.