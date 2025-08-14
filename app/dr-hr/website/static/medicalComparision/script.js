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
      fetch('/service/ai/sql_hr', {
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
            return `#Employee(id, name, department_id, hire_date, job_title, salary, bonus, experience, date_of_birth, email_id, address)
            #Department(id, name, address, founded, company_type, total_employees, annual_revenue, industry_sector)
            #Salary_Payments(id, employee_id, amount, date, payment_reference, payment_method, deduction_amount, bonus_amount)
            #Contracts(id, employee_id, start_date, end_date, job_title, salary)
            #Time_Sheets(id, employee_id, day, hours_worked)`;
        
        case 'LatestPatient1':
            return `RULE: All employees who have been employed within the last 90 days should have a contract

            RULE: All employees who have worked more than 7 hours per day in the last 2 weeks should have a salary payment
            
            RULE: All salary payments should be recorded in ISO 8601 date format (yyyy-mm-dd)
            
            RULE: Employees in the same department with the same job title must have consistent salary ranges with a maximum difference of 5000 if they have the same experience level.
            
            RULE: Employees should have consistent job titles, salary ranges, and experience levels per department, and no salary payment should be overdue by more than 15 days`;
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