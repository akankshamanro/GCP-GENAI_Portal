
    document.addEventListener("DOMContentLoaded", function () {

      const projectSelector = document.getElementById('projectSelector');


      fetch(CONFIG_FILE)
        .then(response => response.json())
        .then(industryData => {
          // Get the keys (industry names) from the industryData object
          const industryNames = Object.keys(industryData);

      // Iterate through the industry names and create <option> elements
        industryNames.forEach(industryName => {
          const option = document.createElement('option');
          option.value = industryName;
          option.textContent = industryName;
          projectSelector.appendChild(option);
        });

        // Add an event listener to handle the initial selection
      projectSelector.addEventListener('change', redirectToSelectedRoute);
      // Trigger the initial selection event
      projectSelector.dispatchEvent(new Event('change'));
      window.industryData = industryData;

      
     
        });
      
        
      
    });

 

  const industryHeader = document.getElementById("industry-header");
  // Function to update the quick-access items
// Function to update the quick-access items

function updateQuickAccess(industry) {

  fetch(CONFIG_FILE)
        .then(response => response.json())
        .then(industryData => {
          // Get the keys (industry names) from the industryData object
          const industryNames = Object.keys(industryData);
          console.log('Updating quick access for industry: ' + industry);
          industryHeader.textContent = "Welcome to " + industry + " Dashboard";
          const quickAccessContainer = document.getElementById('quick-access');
          quickAccessContainer.innerHTML = ''; // Clear existing items
          
          
          industryData[industry].forEach(result => {
        
            if (result.is_displayed) {
              const quickAccessItem = document.createElement('div');
              quickAccessItem.className = 'quick-access-item';
        
              if (result.is_locked) {
                quickAccessItem.classList.add('locked-item')
                const lockIcon = document.createElement('span');
                lockIcon.className = 'lock-icon';
                lockIcon.innerHTML = '<i class="fa fa-lock"></i>';
                lockIcon.addEventListener('click', () => {
                  alert('This is a restricted app. Please contact the administrator.');
                });
                quickAccessItem.appendChild(lockIcon);
              }
        
              const tagsDiv = document.createElement('div');
              tagsDiv.className = 'tags';
        
              // Display tags as pills
        
              result.tags.forEach(tag => {
                const tagPill = document.createElement('span');
                tagPill.className = 'tag-pill';
                tagPill.textContent = tag;
                tagsDiv.appendChild(tagPill);
              });
        
         
        
              const link = document.createElement('a');
              if (result.is_locked || !result.is_active) {
                link.addEventListener('click', (event) => {
                  event.preventDefault();
                  alert('This is a restricted app. Please contact the administrator.');
                });
              } else if (result.static_link) {
                link.href = result.static_link;
              } else {
                link.href = `/dashboard/${result.route_function}?app_name=${result.app_name}`;
              }
        
              const h3 = document.createElement('h3');
              h3.innerHTML = `<i class="fa-brands fa-confluence"></i> ${result.app_name}`;
        
              const p = document.createElement('p');
        
              p.textContent = result.app_description;
        
              const iconDiv = document.createElement('div');
              iconDiv.className = 'icon';
              const iconImg = document.createElement('img');
              iconImg.src = result.img_icon;
              iconImg.alt = result.img_icon_alt;
              iconDiv.appendChild(iconImg);
        
         
        
              link.appendChild(h3);
              link.appendChild(p);
              link.appendChild(iconDiv);
        
         
        
              quickAccessItem.appendChild(tagsDiv);
              quickAccessItem.appendChild(link);
              quickAccessContainer.appendChild(quickAccessItem);
        
         
              // Add a separator line
              const separatorLine = document.createElement('div');
              separatorLine.className = 'separator-line';
              quickAccessContainer.appendChild(separatorLine);
        
            }
        
            });
        
          })
        }



  // Function to handle the dropdown change event

  function redirectToSelectedRoute() {
    const selectElement = document.getElementById('projectSelector');
    const selectedIndustry = selectElement.options[selectElement.selectedIndex].value;

    // Update the quick-access items based on the selected industry
    updateQuickAccess(selectedIndustry);
  }

  // Check the selected industry and update the quick-access items on page load
  document.addEventListener('DOMContentLoaded', function () {
    redirectToSelectedRoute(); // Initial population
  });

let data;
let result = [];

console.log(CONFIG_FILE);

fetch(CONFIG_FILE)
  .then(response => response.json())
  .then(industryData => {
    // Assign the fetched JSON data to the 'data' variable
    data = industryData;


    // Iterate over each industry in the data
    for (let industry in data) {
      // Iterate over each app in the industry
      for (let app of data[industry]) {
        // Add the static_link to the result array
        result.push(app.static_link);
      }
    }

    // Print the result
    console.log(result);

    // Fetch all links after 'result' is populated
    fetchAllLinks();
  })
  .catch(error => console.error('Error:', error));
// Function to fetch data from each link
async function fetchLink(link) {
  try {
      const response = await fetch(link + '/health');
      const data = await response.json();
      return data;
  } catch (error) {
      console.error('Error:', error);
  }
}

// Function to fetch all links and get an array of responses
async function fetchAllLinks() {
  const responses = await Promise.all(result.map(fetchLink));
  console.log(responses);
}