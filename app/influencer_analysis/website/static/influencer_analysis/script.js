// const infoButton = document.getElementById('info-button');
// const infoPanel = document.getElementById('info-panel');
// const closeButton = document.getElementById('close-button');
// const tableBody = document.getElementById("product-table-body");

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

document.addEventListener("DOMContentLoaded", function () {
    const stylemeToggle = document.getElementById("stylemeToggle");
    const stylemeSubmenu = document.getElementById("stylemeSubmenu");
    
  
    stylemeToggle.addEventListener("click", function (e) {
      e.preventDefault(); // Prevent the link from navigating
      stylemeSubmenu.classList.toggle("active");
    });
  });

// JavaScript
document.addEventListener("DOMContentLoaded", function () {
    const extractButton = document.getElementById("extract-button");
    const tableBody = document.getElementById("product-table-body"); // Get the table body

    extractButton.addEventListener("click", function () {
        const magazine_id = celebData.celebrity_magazine;
        console.log(magazine_id);
        // Define the API URL and request payload
        const apiUrl = "/api/extract-products"; // Updated to use the Flask endpoint
        const requestData = {
            magazine_id: magazine_id
        };

        // An array of sales boost values corresponding to products
        const salesBoosts = [10, 5, 3, 2, 7, 20]; // Add more values as needed

        // Make a POST request to the Flask endpoint
        fetch(apiUrl, {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify(requestData)
        })
            .then((response) => response.json())
            .then((data) => {
                // Clear the existing table body
                tableBody.innerHTML = "";

                // Get the engagement rate from the HTML
                const engagementRateElement = document.getElementById("engagement-rate");
                const engagementRate = parseFloat(engagementRateElement.textContent.match(/([\d.]+)/)[0]);

                // Loop through the API response and create table rows
                data.recommended_products.forEach((product, index) => {
                    const row = tableBody.insertRow();
                    const productCell = row.insertCell(0);
                    const salesBoostCell = row.insertCell(1);

                    // Assign values to the table cells
                    productCell.textContent = product;
                    salesBoostCell.textContent = (salesBoosts[index] * engagementRate).toFixed(2) + "%"; // Multiply by the corresponding sales boost
                });
            })
            .catch((error) => {
                console.error("Error fetching data from the API:", error);
            });
    });
});


  document.addEventListener("DOMContentLoaded", function () {
    const extractButton = document.getElementById("extract-button");
    const productList = document.getElementById("product-list");
  
    extractButton.addEventListener("click", function () {
  
        const magazine_id = celebData.celebrity_magazine;
        console.log(magazine_id);
        // Define the API URL and request payload
        const apiUrl = "/api/extract-products"; // Updated to use the Flask endpoint
        const requestData = {
            magazine_id: magazine_id
        };
  
        // Make a POST request to the Flask endpoint
        fetch(apiUrl, {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify(requestData)
        })
            .then((response) => response.json())
            .then((data) => {
                // Clear the existing product list
                productList.innerHTML = "";
  
                // Loop through the recommended products and create list items
                data.recommended_products.forEach((product) => {
                    const listItem = document.createElement("li");
                    listItem.textContent = product;
                    listItem.classList.add("pill");
                    productList.appendChild(listItem);
                });
            })
            .catch((error) => {
                console.error("Error fetching data from the API:", error);
            });
    });
  });
// Function to generate a random color
function getRandomColor() {
    const letters = "0123456789ABCDEF";
    let color = "#";
    for (let i = 0; i < 6; i++) {
        color += letters[Math.floor(Math.random() * 16)];
    }
    return color;
}

// Get the ul element with the class 'pill-list'
const ulElement = document.getElementById("pill");

// Get all li elements within the ul element
const liElements = ulElement.querySelectorAll("li");

// Apply a random background color to each li element
liElements.forEach((li) => {
    li.style.backgroundColor = getRandomColor(); // Corrected the property name to 'backgroundColor'
});


function redirectToSelectedRoute() {

    var selectElement = document.getElementById("projectSelector");

    var selectedOption = selectElement.options[selectElement.selectedIndex].value;

    // Redirect to the Flask route with the selected option as the industry parameter

    window.location.href = "/dashboard/" + selectedOption;

}
