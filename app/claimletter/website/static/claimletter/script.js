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
function setSampleValue(){

    document.getElementById("medicalProcedure").value = "Insulin Therapy";
    document.getElementById('disease').value = "Diabetes";
}
// Wait for the DOM to be ready
document.addEventListener("DOMContentLoaded", function () {
    // Find the form and button elements by their IDs
    const form = document.getElementById("claimRequestForm");
    const generateButton = document.querySelector(".Generate");
    const letterContainer = document.getElementById("div2"); // Element to display the generated letter

    // Add a submit event listener to the form
    form.addEventListener("submit", function (event) {
        event.preventDefault(); // Prevent the default form submission behavior

        // Serialize the form data into a JSON object
        const formData = new FormData(form);
        const formDataObject = {};
        formData.forEach((value, key) => {
            formDataObject[key] = value;
        });
        var divId = "div2";
        var loaderDiv = document.getElementById(divId).querySelector(".loader");
        loaderDiv.style.display = "block";
        // Send the JSON data to the /generate_letter endpoint
        fetch("/generate_letter", {
            method: "POST",
            body: JSON.stringify({ claimRequestForm: formDataObject }),
            headers: {
                "Content-Type": "application/json",
            },
        })
        .then(response => response.json())
        .then(data => {
             // Hide the loader
             var loaderDiv = document.getElementById(divId).querySelector(".loader");
             loaderDiv.style.display = "none";
            // Handle the response, e.g., format and display the generated letter
            const extracted_info = data.letter;
        
            // Clean up the extracted_info to remove extra whitespace and line breaks
            const cleaned_info = extracted_info.trim().replace(/\n{2,}/g, '\n\n');
        
            // Create a div for the letter content
            const letterContentDiv = document.createElement('div');
            letterContentDiv.innerHTML = cleaned_info;
        
            // Clear the existing content in the letterContainer
            letterContainer.innerHTML = '';
        
            // Append the letter content div to the letterContainer
            letterContainer.appendChild(letterContentDiv);
        
            // Apply CSS to format the letter
            letterContainer.style.whiteSpace = 'pre-line';
        })
        
            
        
        
        .catch(error => {
            console.error("Error:", error);
        });
    });
});

function redirectToSelectedRoute() {

    var selectElement = document.getElementById("projectSelector");

    var selectedOption = selectElement.options[selectElement.selectedIndex].value;

    // Redirect to the Flask route with the selected option as the industry parameter

    window.location.href = "/dashboard/" + selectedOption;

}