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

// Function to submit the customer complaint with loader effect
function submitComplaint() {
    // Get the complaint text from the textarea
    const complaintText = document.getElementById("complaintText").value;

    // Check if the complaint text is not empty
    if (!complaintText) {
        alert("Please enter a complaint.");
        return;
    }

    // Show the loader element
    const loader = document.getElementById("loader");
    loader.style.display = "block";

    // Send the complaint text to the server using fetch
    fetch("/submit_complaint", {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
        },
        body: JSON.stringify({ "complaintText": complaintText })
    })
        .then((response) => response.json())
        .then((data) => {
            // Handle the response or data as needed
            console.log(data); // Log the response from the server

            // Hide the loader element
            loader.style.display = "none";

            // Display the success message
            document.getElementById("successMessage").style.display = "block";

            // Log before setting textContent
            console.log("Generated Text:", data.generated_text);
           
        })
        .catch((error) => {
            // Hide the loader element in case of an error
            loader.style.display = "none";
            console.error("Error:", error);
        });  
       
}
// Function to close the flashing success message
function closeFlashMessage() {
    const successMessage = document.getElementById("successMessage");
    successMessage.style.display = "none";
}

// function generateSummary() {
//     // Get the complaint text from the textarea
//     const complaintText = document.getElementById('complaintText').value;
//     console.log("complaintText", complaintText)
//     // complaintText.replace(/\s+/g, '');
//     // Make an API request to your Cloud Run API
//     // Replace '/submit_complaint' with your actual API endpoint
//     const apiUrl = '/submit_complaint';

//     fetch(apiUrl, {
//         method: 'POST',
//         headers: {
//             'Content-Type': 'application/json'
//         },
//         body: JSON.stringify({ complaintText })
//     })
//     .then(response => response.json())
//     .then(data => {
//         console.log("data***************",data)
//         // Extract and parse JSON content from the generated_text
//         const jsonStart = data.generated_text.indexOf('{');
//         const jsonEnd = data.generated_text.lastIndexOf('}');
//         let jsonString = data.generated_text.slice(jsonStart, jsonEnd + 1);
//         console.log("Joining strings**************", jsonString)
//         let jsonStrings = jsonString.replace(/\s+/g, '').replaceAll('}{', '}|{').split('|')
//         let arr = jsonStrings.map(item => JSON.stringify(JSON.parse(item)))

//         console.log("jsonStrings********",jsonStrings)
//         console.log("arr********",arr)
//         // jsonString = jsonStrings.replaceAll('}{', '}|{').split('|') 

//         // console.log("jsonString*******88",jsonString)
//         // let arr = jsonString.map(item => JSON.parse(item))

//         // console.log("jsonString***********", jsonString)
//         // console.log("jsonString***********", arr)
//         // const generatedData = JSON.parse(jsonString);

//         // console.log("generatedData", generatedData)

//         // Update the table with the parsed product summary

        
//     const productSummary = document.getElementById('productSummary');
//         // for(let i =0;i<arr.length;i++){
//         //     productSummary.children[0].textContent = arr[i].product_id;
//         //     productSummary.children[1].textContent = arr[i].product_name;
//         //     productSummary.children[2].textContent = arr[i].issue;
//         // }
//        // Clear existing rows in the table
//        while (productSummary.children.length > 1) {
//         productSummary.removeChild(productSummary.children[1]);
//     }

//     // Iterate through arr and add data to the table
//     for (let i = 0; i < arr.length; i++) {
//         const rowData = JSON.parse(arr[i]);
//         const newRow = document.createElement('tr');
//         const productIdCell = document.createElement('td');
//         const productNameCell = document.createElement('td');
//         const issueCell = document.createElement('td');

//         productIdCell.textContent = rowData.product_id;
//         productNameCell.textContent = rowData.product_name;
//         //issueCell.textContent = rowData.issue;
//         // Replace whitespace characters with spaces in the "issue" text
//         const formattedIssue = rowData.issue.replace(/\s+/g, '   ');

//         console.log("Formatted Issue:", formattedIssue);

//         issueCell.textContent = formattedIssue;
    
//         newRow.appendChild(productIdCell);
//         newRow.appendChild(productNameCell);
//         newRow.appendChild(issueCell);

//         productSummary.appendChild(newRow);
//     } 

//     })
//     .catch(error => {
//         console.error('Error:', error);
//     });
// }

function generateSummary() {
    // Get the complaint text from the textarea
    const complaintText = document.getElementById('complaintText').value;

    // Show the loader
    const loader = document.querySelector('#productSummary .loader');
    loader.style.display = 'inline-block';

    console.log("complaintText", complaintText)

    // Make an API request to your Cloud Run API
    // Replace '/submit_complaint' with your actual API endpoint
    const apiUrl = '/submit_complaint';

    fetch(apiUrl, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ complaintText })
    })
    .then(response => response.json())
    .then(data => {

        console.log("data***************", data)
        const productSummary = document.getElementById('productSummary');
        // Clear existing rows in the table
        while (productSummary.children.length > 1) {
            productSummary.removeChild(productSummary.children[1]);
        }

//         console.log("data***************",data)
//         // Extract and parse JSON content from the generated_text
//         const jsonStart = data.generated_text.indexOf('{');
//         const jsonEnd = data.generated_text.lastIndexOf('}');
//         const jsonString = data.generated_text.slice(jsonStart, jsonEnd + 1);

//         // Hide the loader
//         loader.style.display = 'none';

//         console.log("Joining strings**************", jsonString)
//         let jsonStrings = jsonString.replace(/\s+/g, '').replaceAll('}{', '}|{').split('|')
//         let arr = jsonStrings.map(item => JSON.stringify(JSON.parse(item)))


        // // Extract and parse JSON content from the generated_text
        // const jsonStart = data.generated_text.indexOf('{');
        // const jsonEnd = data.generated_text.lastIndexOf('}');
        // let jsonString = data.generated_text.slice(jsonStart, jsonEnd + 1);
        // console.log("Joining strings**************", jsonString)
        // let jsonStrings = jsonString.replace(/}{/g, '}|{').replaceAll('}{', '}|{').split('|');
        // let arr = jsonStrings.map(item => JSON.stringify(JSON.parse(item)))

        // console.log("jsonStrings********", jsonStrings)
        // console.log("arr********", arr)

        // Extract and parse JSON content from the generated_text using regex
        const regex = /{[^{}]*}/g;
        const jsonStrings = data.generated_text.match(regex) || []; // Extract JSON objects with spaces

        // Process each JSON object
        const arr = jsonStrings.map(item => {
            try {
                return JSON.stringify(JSON.parse(item));
            } catch (error) {
                console.error('Error parsing JSON:', error);
                return null; // Handle parsing errors gracefully
            }
        });

        console.log("Joining strings**************", arr);


      // Modify your JavaScript code for generating the table
for (let i = 0; i < arr.length; i++) {
    const rowData = JSON.parse(arr[i]);
    
    // Create a new row for each data entry
    const newRow = document.createElement('tr');
    
    // Create cells for each column and set their content
    const productIdCell = document.createElement('td');
    productIdCell.textContent = rowData.product_id;

    const productNameCell = document.createElement('td');
    const productNameContainer = document.createElement('div'); // Create a container div
    productNameContainer.classList.add('product-name-container'); // Add a class to the container
    productNameContainer.textContent = rowData.product_name; // Set the text content

    productNameCell.appendChild(productNameContainer); 

    const issueCell = document.createElement('td');
    const preElement = document.createElement('pre');
    preElement.textContent = rowData.issue.replace(/\s+/g, ' ');
    preElement.classList.add('issue-column');
    issueCell.appendChild(preElement);

    const emailCell = document.createElement('td');
    const generateEmailButton = document.createElement('button');
    generateEmailButton.className = 'email-button';
    generateEmailButton.textContent = 'Generate Email';
    generateEmailButton.addEventListener('click', () => {
        

        generateComplaintEmail(rowData); // Pass the complaint data

        document.getElementById('contactTab').click();
    });
    
    emailCell.appendChild(generateEmailButton);

    // Append the cells to the newRow in the same order as the table headers
    newRow.appendChild(productIdCell);
    newRow.appendChild(productNameCell);
    newRow.appendChild(issueCell);
    newRow.appendChild(emailCell);

    // Append the newRow directly under the table's tbody
    const productSummaryTableBody = document.querySelector('table tbody');
    productSummaryTableBody.appendChild(newRow);
}

// Hide the loader after processing all rows
loader.style.display = 'none';


    })
    .catch(error => {
        console.error('Error:', error);
        // Hide the loader in case of an error
        loader.style.display = 'none';
    });
}



// Add event listeners to "Generate Email" buttons in each row
const generateEmailButtons = document.querySelectorAll('.email-button');
generateEmailButtons.forEach(button => {
    button.addEventListener('click', () => {
        const row = button.closest('tr');
        const rowData = {
            product_id: row.cells[0].textContent,
            product_name: row.cells[1].textContent,
            issue: row.cells[2].textContent
        };
        

        sendRowDataToAPI(rowData);
       
    });
});

// JavaScript code for sending data from a specific row to the Flask API
function sendRowDataToAPI(rowData) {
    
    // Make an API request to your Flask API for generating the email
    fetch('/generate_complaint_email', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ productData: rowData })
    })
    .then(response => response.json())
    .then(data => {
        
        // Get the complaintEmail container element
        const complaintEmailContainer = document.getElementById('complaintEmail');
        complaintEmailContainer.innerHTML = data.complaintEmail;

        document.getElementById('contactTab').click();
        
    })
    .catch(error => {
        console.error('Error:', error);
       
    });
}
// Define the generateComplaintEmail function
function generateComplaintEmail(rowData) {
    // Make an API request to your Flask API for generating the email
    fetch('/generate_complaint_email', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ rowData })
    })
    .then(response => response.json())
    .then(data => {
        // Handle the response from the API as needed
        console.log("Generated Complaint Email:", data.complaintEmail);


        // Display the generated email in the complaintEmail container
        const complaintEmailContainer = document.getElementById('complaintEmail');
        complaintEmailContainer.innerHTML = data.complaintEmail;
    })
    .catch(error => {
        console.error('Error:', error);
    });
}

                      
// function createComplaintEmail() {
//     // Get the complaint text from the textarea
//     const complaintText = document.getElementById("complaintText").value;
//     console.log("complaint*****",complaintText)
//     // Check if the complaint text is not empty
//     if (!complaintText) {
//         alert("Please enter a complaint.");
//         return;
//     }

//     // Send the complaint text to the server using fetch
//     fetch("/create_complaint_email", {
//         method: "POST",
//         headers: {
//             "Content-Type": "application/json",
//         },
//         body: JSON.stringify({"complaintText": complaintText }),
//     })
//     .then((response) => response.json())
//     .then((data) => {
//         // Handle the response data and update the #complaintEmail div
//         const complaintEmailDiv = document.getElementById("complaintEmail");

//         // Extract the email text from the response
//         const emailText = data.complaintEmail;

//         // Split the email text into lines based on the newline character '\n'
//         const lines = emailText.split('\n');

//         // Create a new HTML string with line breaks and special formatting for specific lines
//         let formattedText = '';
//         for (let i = 0; i < lines.length; i++) {
//             const line = lines[i].trim(); // Remove leading and trailing spaces
//             if (line) {
//                 if (
//                     line.startsWith("Product ID:") ||
//                     line.startsWith("Product Name:") ||
//                     line.startsWith("Issue:")
//                 ) {
//                     // Add these lines without an extra line break
//                     formattedText += line + '<br>';
//                 } else if (line.startsWith("The screen has a prominent black line running across it, which ruins my viewing experience.")) {
//                     // Add a space after this specific line
//                     formattedText += line + '<br><br>';
//                 } else {
//                     // Add other lines with a <p> element for line breaks
//                     formattedText += '<p>' + line + '</p>';
//                 }
//             }
//         }

//         // Set the innerHTML of the complaintEmailDiv with the formatted text
//         complaintEmailDiv.innerHTML = formattedText;
//     })

    
//     .catch((error) => {
//         console.error("Error:", error);
//     });
// }

    // JavaScript to toggle the submenu when clicking on "Styleme"
    document.addEventListener("DOMContentLoaded", function () {
        const stylemeToggle = document.getElementById("stylemeToggle");
        const stylemeSubmenu = document.getElementById("stylemeSubmenu");
      
        stylemeToggle.addEventListener("click", function (e) {
          e.preventDefault(); // Prevent the link from navigating
          stylemeSubmenu.classList.toggle("active");
        });
      });
      
      function openPage(pageName, elmnt, color) {
        var i, tabcontent, tablinks;
        tabcontent = document.getElementsByClassName("horizontal-container");
        for (i = 0; i < tabcontent.length; i++) {
          tabcontent[i].style.display = "none";
        }
        tablinks = document.getElementsByClassName("tablink");
        for (i = 0; i < tablinks.length; i++) {
          tablinks[i].style.backgroundColor = "";
        }
        document.getElementById(pageName).style.display = "block";
        elmnt.style.backgroundColor = color;
      }
      
      // Get the element with id="defaultOpen" and click on it
      document.getElementById("defaultOpen").click();
      

// Function to display the complaint text in the textarea
function displayComplaintText() {
    // The provided complaint text
    var samplecomplaintText = `
    1. I recently received the Ultra HD TV, and I'm really disappointed with it. The screen has a prominent black line running across it, which ruins my viewing experience. It's Product ID 98765 for your reference. Additionally, the audio quality is subpar, and the remote control frequently malfunctions, making it frustrating to use.
    2. I ordered the ABC Laptop, but it's causing me a lot of trouble. It frequently freezes, and the keyboard keys keep getting stuck, making it nearly impossible to use for work. The Product ID is 67890 in case you need it. Moreover, the battery life is significantly shorter than what was advertised, and the laptop heats up excessively during normal use.
    3. The Deluxe Coffee Maker I purchased last week is not working properly. It brews terrible-tasting coffee, and it's nothing like what was advertised. I expected better quality. The Product ID for your reference is 24680. Additionally, the coffee maker leaks water from the bottom, and the timer function doesn't work, causing inconvenience every morning.
    4. I ordered a gadget, but it turned out to be a complete disappointment. The screen is all wonky, and it keeps freezing. Honestly, it's frustrating. The product name is GadgetX, and the product ID, in case you need it, is 789ABC. Furthermore, the battery drains too quickly, and the camera quality is far from what was promised in the product description.
    5. I received a package today with a pair of shoes I'd been eagerly waiting for. But guess what? They sent me the wrong size! I ordered a 9, and they sent an 11. This mix-up is causing me a lot of inconvenience. The product ID is JKLMNO, by the way. Additionally, the shoes have scuff marks and appear to be a returned item, which is unacceptable for a brand new purchase.
    6. So, I got this fancy watch delivered, and it's not as fancy as it looked online. The strap broke within a week, and it's losing time like there's no tomorrow. Just so you know, the product name is TimeMaster, and the product ID is 123GHI. Furthermore, the watch face scratches easily, and the water resistance is far below the stated level, making it unsuitable for everyday wear.
    7. I received the Smart Home Security System, and it's been nothing but trouble. The motion sensors don't work correctly, and the mobile app crashes consistently. It's Product ID 456XYZ for your reference. Moreover, the camera's night vision mode is practically useless, and the system's setup instructions are unclear, causing confusion during installation.
    8. The Ultra-Comfortable Sofa, Product ID 123DEF, I ordered arrived with a torn cushion and visible scratches. It's not the quality I expected for the price I paid. Additionally, one of the reclining mechanisms is broken, and the upholstery color does not match what was shown in the catalog, making it a disappointing purchase.
    `;

    var complaintTextarea = document.getElementById("complaintText");
    
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