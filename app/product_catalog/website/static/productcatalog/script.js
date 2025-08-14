// JavaScript to toggle the submenu when clicking on "Styleme"
    document.addEventListener("DOMContentLoaded", function () {
        const stylemeToggle = document.getElementById("stylemeToggle");
        const stylemeSubmenu = document.getElementById("stylemeSubmenu");
      
        stylemeToggle.addEventListener("click", function (e) {
          e.preventDefault(); // Prevent the link from navigating
          stylemeSubmenu.classList.toggle("active");
        });
      });
      

function sendLabelsToAPI() {
    // Capture the labels from the label-container
    const labelContainer = document.getElementById("labelContainer");
    const labelTags = labelContainer.querySelectorAll(".label-tag");

    // Extract the label text and store them in an array
    const labels = Array.from(labelTags).map(label => label.innerText);

    // Concatenate the labels into a single string with spaces
    const query = labels.join(' ');

    // Create a JSON object with the query
    const queryData = {
        "query": query
    };

    // Send a POST request to your Flask endpoint
    fetch('/api/send-labels', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(queryData)
    })
    .then(response => response.json())
    .then(data => {
        // Handle the API response here (display products or perform other actions)
        console.log(data);
        displayProducts(data); // For testing, you can log the response
    })
    .catch(error => {
        console.error('Error:', error);
    });
}




// Add a click event listener to the "Recommended Products" button
const recommendedProductsButton = document.getElementById("recommendedProductsButton");
recommendedProductsButton.addEventListener("click", sendLabelsToAPI);

function displayProducts(products) {
    // Assuming there's an HTML element with the ID "productContainer" to display products
    const productContainer = document.getElementById("productContainer");
    
    // Clear any existing products
    productContainer.innerHTML = '';
    const displayedProducts = products.slice(0, 2);
    // Check if products is defined and not empty
    if (Array.isArray(products) && products.length > 0) {
        // Iterate through the received products and create HTML elements to display them
        displayedProducts.forEach(product => {
            const productDiv = document.createElement('div');
            productDiv.className = 'product';
            productDiv.innerHTML = `
                <a href="#" style="text-decoration: none;">
                    <img src="${product.image_URL}" alt="${product.product_name}">
                    <h2 style="color:black;  ">${product.product_name}</h2>
                    <p style="color:black; text-decoration: none; ">$${product.price}</p>
                    
                </a>`;
            productContainer.appendChild(productDiv);
        });
    } else {
        // If no products are available, display a message or handle it as needed
        productContainer.innerHTML = '<p>No products available</p>';
    }
}







    // ... (your existing JavaScript code)

    // Function to make an AJAX request to the /promo route
    function fetchPromotionalText() {
        // Show the loader
    const labelLoader = document.getElementById("labelLoader");
    labelLoader.style.display = "block";
        // Make an AJAX request to your Flask route
        fetch('/promo')
            .then(response => response.json())
            .then(data => {
                // Display the promotional text in the #promoResponse element
                document.getElementById('promoResponse').innerHTML = data;
                // Hide the loader after labels are fetched
        labelLoader.style.display = "none";
            })
            .catch(error => {
                console.error('Error fetching promotional text:', error);
                // Hide the loader after labels are fetched
        labelLoader.style.display = "none";
            });
    }

    // Add an event listener to the "Promotional Text" button
    document.getElementById('promotionalTextButton').addEventListener('click', fetchPromotionalText);


// ... (your existing JavaScript code)

    // Function to make an AJAX request to the /promo route
    function fetchPromotionalTag() {
          // Show the loader
    const labelLoader = document.getElementById("labelLoader");
    labelLoader.style.display = "block";
        // Make an AJAX request to your Flask route
        fetch('/promotag')
            .then(response => response.json())
            .then(data => {
                console.log(data);
                // Check if the 'promotion_tag' field exists in the JSON response
                if (data.hasOwnProperty('promotion_tag')) {
                    // Extract the 'promotion_tag' and display it in the #promoResponse element
                    var promotionTagValue = data.promotion_tag;
                    document.getElementById('promoResponse').innerHTML = promotionTagValue;
                     // Hide the loader after labels are fetched
                    labelLoader.style.display = "none";
                } else {
                    console.error('Promotion tag not found in the response.');
                }
            })
            .catch(error => {
                console.error('Error fetching promotional text:', error);
                 // Hide the loader after labels are fetched
                labelLoader.style.display = "none";
            });
    }
    
    // Add an event listener to the "Create Tagline" button
    document.getElementById('promotionalTagButton').addEventListener('click', fetchPromotionalTag);
    


    const profilePic = document.getElementById("profile-pic");
    const inputFile = document.getElementById("input-file");
    const analyzeButton = document.getElementById("analyze-button");
    
    // Function to update the profile picture when a new image is selected
    inputFile.addEventListener("change", function () {
        if (inputFile.files.length > 0) {
            const selectedImage = inputFile.files[0];
            const objectURL = URL.createObjectURL(selectedImage);
            profilePic.src = objectURL;
    
            // Store the updated image URL in local storage
            localStorage.setItem("profileImageURL", objectURL);
    
            // Enable the "Upload" button
            analyzeButton.disabled = false;
        } else {
            // No image selected, disable the "Upload" button
            analyzeButton.disabled = true;
        }
    });
    
    // Function to submit the form
    function submitForm() {
        const form = document.createElement("form");
        form.method = "post";
        form.enctype = "multipart/form-data";
        form.action = "/product_tag";
    
        const fileInput = document.createElement("input");
        fileInput.type = "file";
        fileInput.name = "file";
        fileInput.accept = "image/jpeg, image/png, image/jpg";
        fileInput.files = inputFile.files;
    
        form.appendChild(fileInput);
        document.body.appendChild(form);
        form.submit();
    }
    
    // Add an event listener to the "Upload" button to trigger the form submission
    analyzeButton.addEventListener("click", function () {
        // Check if an image is selected before allowing the form submission
        if (inputFile.files.length > 0) {
            // Trigger the form submission when the button is clicked
            submitForm();
    
            // Disable the "Upload" button after submission
            analyzeButton.disabled = true;
        }
    });
    
    // Disable the "Upload" button initially when the page loads
    analyzeButton.disabled = true;
    
    // Check if an image was previously selected and enable the button accordingly during page load
    const savedImageURL = localStorage.getItem("profileImageURL");
    if (savedImageURL) {
        profilePic.src = savedImageURL;
    }
    
// Function to generate a random color
function getRandomColor() {
    const letters = "0123456789ABCDEF";
    let color = "#";
    for (let i = 0; i < 6; i++) {
        color += letters[Math.floor(Math.random() * 16)];
    }
    return color;
}

// Get all label-tag elements
const labelTags = document.querySelectorAll(".label-tag");

// Apply a random background color to each label-tag
labelTags.forEach((tag) => {
    tag.style.backgroundColor = getRandomColor();
});

const wrapper = document.querySelector(".wrapper");
const fileName = document.querySelector(".file-name");
const defaultBtn = document.querySelector("#default-btn");
const customBtn = document.querySelector("#custom-btn");
const cancelBtn = document.querySelector("#cancel-btn i");
const img = document.querySelector("img");
let regExp = /[0-9a-zA-Z\^\&\'\@\{\}\[\]\,\$\=\!\-\#\(\)\.\%\+\~\_ ]+$/;
function defaultBtnActive(){
  defaultBtn.click();
}
defaultBtn.addEventListener("change", function(){
  const file = this.files[0];
  if(file){
    const reader = new FileReader();
    reader.onload = function(){
      const result = reader.result;
      img.src = result;
      wrapper.classList.add("active");
    }
    cancelBtn.addEventListener("click", function(){
      img.src = "";
      wrapper.classList.remove("active");
    })
    reader.readAsDataURL(file);
  }
  if(this.value){
    let valueStore = this.value.match(regExp);
    fileName.textContent = valueStore;
  }
});

function redirectToSelectedRoute() {

    var selectElement = document.getElementById("projectSelector");

    var selectedOption = selectElement.options[selectElement.selectedIndex].value;

    // Redirect to the Flask route with the selected option as the industry parameter

    window.location.href = "/dashboard/" + selectedOption;

}