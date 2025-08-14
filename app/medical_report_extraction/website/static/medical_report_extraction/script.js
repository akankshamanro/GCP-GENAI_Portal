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

function submitForm(event) {
  event.preventDefault(); // Prevent the default form submission behavior

  // Get the medical report text from the form
  var medicalReport = document.querySelector('textarea[name="medical_report"]').value;

  // Create a JSON object with the medical report
  var data = {
    medical_report: medicalReport
  };

  // Show loader in right-div
  for (var i = 1; i <= 6; i++) {
    var divId = "div" + i;
    var loaderDiv = document.getElementById(divId).querySelector(".loader");
    loaderDiv.style.display = "block";
  }

  // Send the data to your Flask route using fetch
  fetch('/extract_medreport_info', {
    method: 'POST',
    body: JSON.stringify(data),
    headers: {
      'Content-Type': 'application/json'
    }
  })
  .then(response => response.json())
  .then(apiResponse => {
    // Handle the API response here
    console.log(apiResponse);

    // Assuming you have a function to update the six divs with the response
    updateDivs(apiResponse);

    // Hide loader in right-div
    for (var i = 1; i <= 6; i++) {
      var divId = "div" + i;
      var loaderDiv = document.getElementById(divId).querySelector(".loader");
      loaderDiv.style.display = "none";
    }
  })
  .catch(error => {
    console.error('Error:', error);
  });
}

    // Function to update the six divs with the extracted information
    function updateDivs(apiResponse) {
        // Split the extracted information into lines
        var lines = apiResponse.extracted_info.split('\n');

        // Populate the six divs with the extracted information
        for (var i = 0; i < 6; i++) {
            var divId = "div" + (i + 1);
            var div = document.getElementById(divId);
            if (i < lines.length) {
                div.textContent = lines[i];
            } else {
                div.textContent = ""; // Clear any remaining divs
            }
        }
    }

    function clearTextarea() {
        document.querySelector('textarea[name="medical_report"]').value = "";
    }

    // Function to display the complaint text in the textarea
function displayComplaintText() {
    // The provided complaint text
    var samplecomplaintText = `
    Certainly, here is the medical report with additional information included:

[Medical Report]

Patient Information:
Name: John Smith
Date of Birth: 01/15/1980
Gender: Male
Medical Record Number: MRN123456
Date of Examination: 09/26/2023

1. Pre-existing Condition:
The patient has a history of the following pre-existing conditions:
- Hypertension
  - Diagnosed in 2010
  - Previous treatment with Lisinopril and Atenolol
- Type 2 Diabetes
  - Diagnosed in 2015
  - Previously managed with Metformin and dietary modifications

2. Current Medication:
At the time of this examination, the patient is taking the following medications:
- Lisinopril (10 mg) for hypertension, once daily
  - Started in 2010
- Metformin (1000 mg) for diabetes, twice daily
  - Started in 2015

3. Current Symptoms:
The patient presented with the following symptoms during the examination:
- High blood pressure (160/90 mm Hg)
  - Persistent despite current medication
- Fatigue
  - Reports feeling tired most of the time
- Frequent urination
  - Experiencing increased urinary frequency and thirst

4. Diagnosis:
Based on the patient's medical history, physical examination, and diagnostic tests, the following diagnosis has been made:
- Uncontrolled hypertension
  - Elevated blood pressure readings despite current treatment
- Type 2 Diabetes Mellitus
  - Continued symptoms of polyuria and fatigue, indicative of uncontrolled diabetes

5. Prescribed Drug:
To address the diagnosed conditions and alleviate the current symptoms, the following medication has been prescribed:
- Amlodipine (5 mg) for hypertension
  - Dosage: 5 mg once daily
  - Frequency: Once daily
  - Route of Administration: Oral
  - Duration: Ongoing
  - Lifestyle modifications recommended, including sodium restriction and increased physical activity

6. Alternative Drug:
In the event of any contraindications, allergies, or intolerances to the prescribed medication, an alternative drug that can be considered is:
- Hydrochlorothiazide (12.5 mg) for hypertension
  - Dosage: 12.5 mg once daily
  - Frequency: Once daily
  - Route of Administration: Oral
  - Duration: Ongoing

Additional Information:
- The patient's BMI is 32, indicating overweight status.
- Advised the patient to follow a diabetic diet and monitor blood glucose regularly.
- Scheduled a follow-up appointment in three weeks to assess the response to treatment and adjust the medication regimen as needed.

Please note that this medical report is based on the information available at the time of the examination. It is essential for the patient to follow the prescribed treatment plan and medication regimen. Any adverse reactions or changes in the patient's condition should be reported promptly to their healthcare provider. This report is confidential and is intended solely for the use of the patient and their healthcare team.

Signature: Dr. Sarah Johnson
Medical License Number: MD123456
Date: 09/26/2023`;

    var complaintTextarea = document.getElementById("medical_report");
    
    // Populate the textarea with the complaint text
    complaintTextarea.value = samplecomplaintText;
    
    // Display the textarea if it's not already displayed
    if (complaintTextarea.style.display === "none" || complaintTextarea.style.display === "") {
        complaintTextarea.style.display = "block";
    }
}


function redirectToSelectedRoute() {

  var selectElement = document.getElementById("projectSelector");

  var selectedOption = selectElement.options[selectElement.selectedIndex].value;

  // Redirect to the Flask route with the selected option as the industry parameter

  window.location.href = "/dashboard/" + selectedOption;

}