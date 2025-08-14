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
      fetch('/service/ai/sql_retail', {
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
            return `#Product(id, name, category_id, brand_id, supplier_id, price, quantity, description, image, creation_date, discount, stock_threshold)
            #Category(id, name, description)
            #Brand(id, name, description)
            #Supplier(id, name, email_id, contact_number, address, contract_start_date, contract_end_date)
            #Store(id, name, address, city, zipcode, contact_number, email_id, opening_hours, manager_id)
            #Employee(id, name, store_id, hire_date, job_title, contact, email_id, date_of_birth, address)
            #Sales(id, transaction_id, store_id, employee_id, product_id, date, quantity, total_amount, payment_method)
            #Inventory_Transaction(id, store_id, product_id, transaction_date, transaction_type, old_stock_level, new_stock_level, supplier_id)
            #Customer(id, name, address, city, zipcode, contact_number, email_id, registration_date)
            #Discounts(id, product_id, store_id, type, start_date, end_date, value)
            #Sales_Return(id, transaction_id, store_id, product_id, date, quantity, reason)`;
        
        case 'LatestPatient1':
            return `all sold products have a valid category and brand assigned, and all sales transactions have valid store and employee ids


            no sales transactions with a total amount less than the sum of the products' prices (which might indicate pricing errors or calculation issues).
            
            
            no products are sold with a negative inventory level in a store (which might indicate inventory mismanagement or data entry issues)
            
            
            no sales transactions where the product's discount was not applied if there was an active discount for the purchased product during the sale date`;
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