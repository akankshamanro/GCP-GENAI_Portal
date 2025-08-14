
function submitForm(event) {
    event.preventDefault(); // Prevent the default form submission behavior
 
    // Get the medical report text from the form
    var medicalReport = document.querySelector('textarea[name="medical_report"]').value;
 
    // Create a JSON object with the medical report
    var data = {
        notes: medicalReport
    };
 
    // Show loader in right-div
    for (var i = 1; i <= 4; i++) {
        var divId = "div" + i;
        var loaderDiv = document.getElementById(divId).querySelector(".loader");
        loaderDiv.style.display = "block";
    }
 
    // Send the data to your Flask route using fetch
    fetch('/generate_answers', {
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
            for (var i = 1; i <= 4; i++) {
                var divId = "div" + i;
                var loaderDiv = document.getElementById(divId).querySelector(".loader");
                loaderDiv.style.display = "none";
            }
        })
        .catch(error => {
            console.error('Error:', error);
        });
}
 
// Function to update the divs with the extracted information
function updateDivs(apiResponse) {
    var answers = apiResponse.answers;
    // Assuming apiResponse is an array of strings
    for (var i = 0; i < answers.length; i++) {
        var divId = "div" + (i + 1);
        var div = document.getElementById(divId);
 
        // Clear the existing content of the div
        div.innerHTML = '';
        // Split the response by '\n' to separate bullet points
        var bulletPoints = answers[i].split('\n');
 
        // Create an unordered list to hold the bullet points
        var ul = document.createElement("ul");
 
        // Populate the list with bullet points
        bulletPoints.forEach(function(point) {
            var li = document.createElement("li");
            li.textContent = point;
            ul.appendChild(li);
        });
 
        // Append the list to the div
        div.appendChild(ul);
    }
}
 
function clearTextarea() {
    document.querySelector('textarea[name="medical_report"]').value = "";
}
 
// Function to display the complaint text in the textarea
function displayComplaintText() {
    // The provided complaint text
    var samplecomplaintText = `
        "In our recent equipment inspection, several issues were detected across different component types. The main findings include electrical faults in the power distribution unit, coolant leakage in the cooling system, and irregular temperature fluctuations in the processing unit. To address these problems, immediate resolution actions were taken. For instance, we replaced the damaged cables in the power distribution unit, applied sealants to fix the coolant leaks, and recalibrated the temperature sensors in the processing unit. These issues were deemed critical due to their potential to disrupt production. As for preventive maintenance recommendations, the notes suggest regular coolant system inspections, voltage stability checks, and temperature sensor replacements as part of our ongoing maintenance strategy.`;
 
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

