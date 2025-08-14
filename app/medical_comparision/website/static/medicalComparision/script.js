// const infoButton = document.getElementById('info-button');
// const infoPanel = document.getElementById('info-panel');
// const closeButton = document.getElementById('close-button');

// infoButton.addEventListener('click', () => {
//     infoPanel.style.right = '0';
// });

// closeButton.addEventListener('click', () => {
//     infoPanel.style.right = '-500px';
// });


// // Select all elements with the "i" tag and store them in a NodeList called "stars"
// const stars = document.querySelectorAll(".stars i");
// // Loop through the "stars" NodeList
// stars.forEach((star, index1) => {
//   // Add an event listener that runs a function when the "click" event is triggered
//   star.addEventListener("click", () => {
//     // Loop through the "stars" NodeList Again
//     stars.forEach((star, index2) => {
//       // Add the "active" class to the clicked star and any stars with a lower index
//       // and remove the "active" class from any stars with a higher index
//       index1 >= index2 ? star.classList.add("active") : star.classList.remove("active");
//     });
//   });
// });

document.addEventListener('DOMContentLoaded', function () {
    const form = document.getElementById('medicalRecordsForm');
  
    form.addEventListener('submit', function (e) {
      e.preventDefault(); // Prevent the default form submission behavior
  
      // Get the input values
      const previousRecord = document.getElementById('previousRecord').value;
      const latestRecord = document.getElementById('latestRecord').value;
  
      // Create a JSON object with the input values
      const medicalRecords = {
        "previous_medical_record": previousRecord,
        "latest_medical_record": latestRecord
      };
  
      // Convert the JSON object to a JSON string
      const recordsJson = JSON.stringify(medicalRecords);
      var divId = "div2";
      var loaderDiv = document.getElementById(divId).querySelector(".loader");
      loaderDiv.style.display = "block";
      // Make an HTTP POST request to your Flask endpoint
      fetch('https://gen-ai-service-retail-kcvokjzgdq-ew.a.run.app/service/ai/compare_medical_records', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: recordsJson,
      })
        .then(response => response.text()) // Get the response as a text string
        .then(data => {
            try {
                console.log('Raw Response: ', data);

                // Remove double quotes from the response
                const cleanData = data.replace(/"/g, '');

                // Set the content of div2 with line breaks and indentation
                const div2 = document.getElementById('div2');
                div2.innerHTML = cleanData;

                // Hide the loader
                var loaderDiv = document.getElementById(divId).querySelector(".loader");
                loaderDiv.style.display = "none";
            } catch (error) {
                console.error('Error:', error);
                // Handle any error here
            }
        })
        .catch(error => {
            console.error('API Error:', error);
            // Handle errors here
        });
    });
});

  function myFunction(dropdownId) {
    var dropdownContent = document.getElementById(dropdownId);
    dropdownContent.classList.toggle("show");
}

// Function to select a patient and update the textarea content
function selectPatient(patientName) {
    var previousTextarea = document.getElementById('previousRecord');
    var latestTextarea = document.getElementById('latestRecord');
    
    // Replace this with the text you want to display for each patient
    var patientText = getPatientText(patientName);

    // Check if it's a "Latest" patient
    if (patientName.startsWith('Latest')) {
        latestTextarea.value = patientText;
    } else {
        previousTextarea.value = patientText;
        // Also populate the latestTextarea with the corresponding "Latest" patient's notes
        var latestPatientName = 'Latest' + patientName;
        var latestPatientText = getPatientText(latestPatientName);
        latestTextarea.value = latestPatientText;
    }
    
    // Close the dropdown after selection
    var dropdowns = document.getElementsByClassName("dropdown-content");
    for (var i = 0; i < dropdowns.length; i++) {
        dropdowns[i].classList.remove('show');
    }
}

function getPatientText(patientName) {
    // You can define different text for each patient here
    switch (patientName) {
        case 'Patient1':
            return `Patient Information:
    Name: John Doe
    Date of Birth: January 15, 1980
    Gender: Male
    Medical Record Number: 12345
    Contact Information: johndoe@email.com, (123) 456-7890
    Medical History:
    - Hypertension
    - Type 2 Diabetes
    - Allergic to Penicillin
    Medications and Treatments:
    - Medication: Lisinopril (10mg daily)
    - Treatment Plan: Diet and exercise for diabetes management
    - Previous Medications: Metformin (discontinued 6 months ago)
    Vital Signs:
    - Blood Pressure: 140/90 mmHg
    - Heart Rate: 80 bpm
    - Temperature: 98.6°F
    - Weight: 180 lbs
    Laboratory Results:
    - Blood Glucose: 160 mg/dL
    - Hemoglobin A1c: 7.2%
    - Cholesterol: LDL 130 mg/dL, HDL 40 mg/dL
    Diagnosis and Progress Notes:
    - Diagnosis: Hypertension and Type 2 Diabetes
    - Last Visit: 3 months ago
    - Progress Note: Blood pressure stable, diabetes under control with diet and Lisinopril.
    Procedures and Surgeries:
    - None
    Family Medical History:
    - Father had Type 2 Diabetes
    - Mother had Hypertension
    Social History:
    - Non-smoker
    - Occasional alcohol consumption
    - Exercises 3 times a week
    Psychosocial History:
    - No known mental health issues
    Insurance Information:
    - Insurance Provider: XYZ Health
    - Policy Number: ABC123456
    - Coverage: General medical care`;
        case 'Patient2':
            return `Patient Note 1: Initial Visit 06/01/2023
        
    Patient Information:
    Name: John Smith
    Age: 55
    Gender: Male
    
    Chief Complaint:
    The patient presents today with a complaint of reduced exercise tolerance and overall decreased physical fitness.
    
    History of Present Illness:
    John Smith is a 55-year-old male who has been relatively active throughout his adult life. He reports that over the past six months, he has noticed a gradual decline in his ability to engage in physical activities. He experiences fatigue and shortness of breath with minimal exertion, such as climbing stairs or walking for more than a few minutes. He denies any chest pain or palpitations. Mr. Smith reports no recent illness, injury, or change in medication.
    
    Past Medical History:
    - Hypertension (controlled with medication)
    - Hyperlipidemia
    - Overweight (BMI 28)
    
    Social History:
    - Non-smoker
    - Sedentary job
    - Occasional alcohol consumption
    
    Family History:
    - Father: Hypertension
    - Mother: Hyperlipidemia
    
    Physical Examination:
    General: Well-developed, overweight male appearing his stated age. Alert and oriented.
    Vital signs: Blood pressure 138/86 mmHg, heart rate 78 bpm, respiratory rate 18 bpm, temperature 98.6°F (37°C)
    Cardiovascular: Regular rate and rhythm, no murmurs, rubs, or gallops
    Respiratory: Clear breath sounds bilaterally, no wheezes or crackles
    Abdomen: Soft, non-tender, non-distended
    Extremities: No edema, no clubbing or cyanosis
    
    Assessment and Plan:
    Based on the patient's history and physical examination, it appears that Mr. Smith is experiencing detraining, resulting in reduced exercise tolerance and decreased physical fitness. The likely contributing factors include a sedentary lifestyle and age-related physiological changes. To further evaluate his condition, the following tests and investigations are ordered:
    
    1. Laboratory Tests:
    - Complete blood count (CBC)
    - Lipid profile
    - Fasting blood glucose
    - Thyroid-stimulating hormone (TSH)
    - Renal function panel
    
    2. Exercise Stress Test:
    To assess his exercise capacity and identify any underlying cardiac abnormalities.
    
    3. Pulmonary Function Tests:
    To evaluate lung function and rule out any obstructive or restrictive pulmonary conditions.
    
    4. Nutritional Consultation:
    To discuss weight management strategies and dietary modifications that can support physical fitness.
    
    Patient education will also be provided, emphasizing the importance of regular physical activity, a balanced diet, and appropriate stress management techniques. A follow-up appointment will be scheduled in two weeks to discuss the test results and formulate a comprehensive management plan.
    `;
        case 'LatestPatient1':
            return `Patient Information:
    Name: John Doe
    Date of Birth: January 15, 1980
    Gender: Male
    Medical Record Number: 12345
    Contact Information: johndoe@email.com, (123) 456-7890
    Medical History:
    - Hypertension
    - Type 2 Diabetes
    - Allergic to Penicillin
    Medications and Treatments:
    - Medication: Lisinopril (10mg daily)
    - Treatment Plan: Diet and exercise for diabetes management
    - No changes in medications or treatment plan.
    Vital Signs:
    - Blood Pressure: 138/88 mmHg (Slight improvement)
    - Heart Rate: 78 bpm
    - Temperature: 98.7°F
    - Weight: 178 lbs (Lost 2 lbs)
    Laboratory Results:
    - Blood Glucose: 150 mg/dL (Slight improvement)
    - Hemoglobin A1c: 7.0% (Slight improvement)
    - Cholesterol: LDL 128 mg/dL, HDL 42 mg/dL (Slight improvements)
    Diagnosis and Progress Notes:
    - Diagnosis: Hypertension and Type 2 Diabetes
    - Current Visit: 3 months later
    - Progress Note: Blood pressure and diabetes show slight improvement. Patient continues to follow treatment plan.
    Procedures and Surgeries:
    - None
    Family Medical History:
    - Father had Type 2 Diabetes
    - Mother had Hypertension
    Social History:
    - Non-smoker
    - Occasional alcohol consumption
    - Exercises 4 times a week (Increased activity)
    Psychosocial History:
    - No known mental health issues
    Insurance Information:
    - Insurance Provider: XYZ Health
    - Policy Number: ABC123456
    - Coverage: General medical care`;
        case 'LatestPatient2':
            return `Patient Note 2: Follow-Up Visit 06/06/2023
            
    Patient Information:
    Name: John Smith
    Age: 55
    Gender: Male

    Chief Complaint:
    The patient returns for a follow-up visit, concerned about his continued decline in exercise tolerance and overall physical fitness.

    History of Present Illness:
    John Smith reports that despite his efforts to incorporate physical activity and make dietary modifications, he continues to experience a decline in exercise capacity. He describes increased fatigue, difficulty performing daily activities, and shortness of breath with minimal exertion. He denies any recent illness or changes in medication.

    Review of Systems:
    - Cardiovascular: No chest pain or palpitations
    - Respiratory: No cough, wheezing, or sputum production
    - Gastrointestinal: No abdominal pain or changes in bowel habits
    - Neurological: No focal weakness or sensory disturbances
    - Musculoskeletal: No joint pain or stiffness

    Physical Examination:
    General: Overweight male appearing his stated age, fatigued
    Vital signs: Blood pressure 140/88 mmHg, heart

    rate 82 bpm, respiratory rate 20 bpm, temperature 98.4°F (36.9°C)
    Cardiovascular: Regular rate and rhythm, no murmurs, rubs, or gallops
    Respiratory: Clear breath sounds bilaterally, no wheezes or crackles
    Abdomen: Soft, non-tender, non-distended
    Extremities: No edema, no clubbing or cyanosis

    Assessment and Plan:
    Despite lifestyle modifications, Mr. Smith's exercise tolerance and physical fitness have continued to decline. The patient's test results from the previous visit are as follows:

    1. Laboratory Results (6 Months Ago):
    - CBC: Within normal limits
    - Lipid profile: Total cholesterol 230 mg/dL (elevated), HDL cholesterol 45 mg/dL (low), LDL cholesterol 160 mg/dL (elevated)
    - Fasting blood glucose: 110 mg/dL (prediabetic)
    - TSH: Within normal limits
    - Renal function panel: Within normal limits

    2. Exercise Stress Test (6 Months Ago):
    The test revealed a reduced exercise capacity compared to age-matched norms. No significant cardiac abnormalities were detected.

    3. Pulmonary Function Tests (6 Months Ago):
    The test results demonstrated no significant pulmonary abnormalities.

    Given the patient's persistent symptoms and continued decline, further investigations are warranted:

    1. Cardiac Imaging:
    - Echocardiography: To assess cardiac structure and function, looking for possible subtle changes over time.

    2. Consultation with a Cardiologist:
    To evaluate the need for additional cardiac tests, such as a nuclear stress test or coronary angiography.

    3. Consultation with a Pulmonologist:
    To assess for any underlying pulmonary conditions that might contribute to his symptoms.

    4. Repeat Laboratory Tests:
    - CBC
    - Lipid profile
    - Fasting blood glucose

    The patient will be scheduled for the recommended consultations and tests. In the meantime, he will be advised to continue with his efforts to incorporate physical activity, maintain a balanced diet, and manage stress appropriately. A follow-up appointment will be scheduled to discuss the test results and formulate a comprehensive management plan.`;
        default:
            return 'No text available.';
    }
}

// Close the dropdown if the user clicks outside of it
window.onclick = function (event) {
    if (!event.target.matches('.dropbtn')) {
        var dropdowns = document.getElementsByClassName("dropdown-content");
        for (var i = 0; i < dropdowns.length; i++) {
            var openDropdown = dropdowns[i];
            if (openDropdown.classList.contains('show')) {
                openDropdown.classList.remove('show');
            }
        }
    }
}

function redirectToSelectedRoute() {

    var selectElement = document.getElementById("projectSelector");

    var selectedOption = selectElement.options[selectElement.selectedIndex].value;

    // Redirect to the Flask route with the selected option as the industry parameter

    window.location.href = "/dashboard/" + selectedOption;

}