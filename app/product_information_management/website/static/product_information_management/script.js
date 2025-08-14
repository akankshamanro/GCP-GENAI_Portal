

function submitForm(event) {
  event.preventDefault(); // Prevent the default form submission behavior

  // Get the medical report text from the form
  var productDescription = document.querySelector('textarea[name="product_description"]').value;

  // Create a JSON object with the medical report
  var data = {
      product_description: productDescription
  };

  // Show loader in right-div
  for (var i = 1; i <= 7; i++) {
      var divId = "div" + i;
      var loaderDiv = document.getElementById(divId).querySelector(".loader");
      loaderDiv.style.display = "block";
  }

  // Send the data to your Flask route using fetch
  fetch('/extract_info', {
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
      for (var i = 1; i <= 7; i++) {
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
var results = apiResponse.results; // Extract the 'results' array

for (var i = 0; i < results.length; i++) {
  var divId = "div" + (i + 1);
  var div = document.getElementById(divId);

  // Check if the div with the given ID exists
  if (div) {
      // Clear the existing content of the div
      div.innerHTML = '';

      // Split the response by '\n' to separate bullet points
      var bulletPoints = results[i].split('\n');

      // Create an unordered list to hold the bullet points
      var ul = document.createElement("ul");

      // Populate the list with bullet points
      bulletPoints.forEach(function (point) {
          if (point.trim() !== "") { // Ignore empty lines
              var li = document.createElement("li");
              li.textContent = point;
              ul.appendChild(li);
          }
      });

      // Append the list to the div
      div.appendChild(ul);
  }
}
}

function clearTextarea() {
  document.querySelector('textarea[name="product_description"]').value = "";
}

// Function to display the complaint text in the textarea
function displayComplaintText() {
// The provided complaint text
var samplecomplaintText = `
ProductName:**Introducingthe'UltiGuard Pro-X 5000'Multi-PurposeToolbox**ProductCategory:**ToolsandEquipment**ProductMaterial:**Constructedwithhigh-grade,durablestainlesssteelforlong-lastingperformanceandreliability.**TargetSegment:**TheUltiGuardPro-X5000isdesignedtomeettheneedsofprofessionalsandDIYenthusiastsalike.Whetheryou're a seasoned tradesperson, a weekend warrior, or a homeowner looking for a versatile toolbox, this product is tailored to your requirements.  **Functional Features:** 1. **Ample Storage:** The UltiGuard Pro-X 5000 boasts spacious compartments and drawers to keep your tools organized and easily accessible.  2. **Heavy-Duty Wheels:** Equipped with heavy-duty swivel wheels for effortless maneuverability, even when fully loaded.  3. **Locking Mechanism:** A secure locking system ensures the safety of your valuable tools, giving you peace of mind on the job site or at home.  
4. **Weather-Resistant:** Built to withstand the elements, this toolbox is designed to protect your tools from rust and moisture.  5. **Telescopic Handle:** The telescopic handle with a comfortable grip allows for convenient transportation.  **Feature Benefits:** - **Efficiency:** With the UltiGuard Pro-X 5000, you can easily access the right tool when you need it, saving you time and effort.  - **Durability:** Crafted from premium stainless steel, this toolbox is built to last, making it a wise investment for your tool collection.  - **Versatility:** Its multifunctional design caters to various tool types and sizes, making it suitable for a wide range of applications.  - **Mobility:** The heavy-duty wheels and telescopic handle make it easy to transport your tools, even across uneven terrain.  - **Security:** Rest assured that your tools are safe and secure with the reliable locking mechanism, 
preventing unauthorized access.  **Product Price:** The UltiGuard Pro-X 5000 is priced competitively at $249.99, offering exceptional value for its quality and features.  ---  **Additional Information:**  - **Dimensions:** The toolbox measures 32 inches in width, 18 inches in depth, and 24 inches in height, providing ample storage space for your tools.  - **Weight Capacity:** With a robust weight capacity of 250 pounds, you can store both lightweight and heavy tools with confidence.  - **Accessories Included:** The UltiGuard Pro-X 5000 comes with a set of dividers and organizers to customize the interior layout according to your specific needs.  - **Warranty:** We stand behind the quality of our product with a 3-year warranty, ensuring your satisfaction and peace of mind.  - **Customer Reviews:** Don'tjusttakeourwordforit.ReadtheravereviewsfromsatisfiedcustomerswhohaveexperiencedtheconvenienceanddurabilityoftheUltiGuardPro-X5000.
UpgradeyourtoolstoragewiththeUltiGuardPro-X5000,thetoolboxthatcombinesfunctionality,durability,andaffordabilityforprofessionalsandDIYenthusiastsalike.Investinthebest,andelevateyourtoolorganizationandtransportationtothenextlevel.`;

var complaintTextarea = document.getElementById("product_description");

// Populate the textarea with the complaint text
complaintTextarea.value = samplecomplaintText;

// Display the textarea if it's not already displayed
if (complaintTextarea.style.display === "none" || complaintTextarea.style.display === "") {
  complaintTextarea.style.display = "block";
}
}

