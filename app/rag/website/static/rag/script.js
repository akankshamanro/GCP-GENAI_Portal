let searchResults = [
    { filename: 'file1.txt', content: 'Content of file1' },
    { filename: 'file2.txt', content: 'Content of file2' },
    { filename: 'file3.txt', content: 'Content of file3' },
    // Add more results as needed
];
 
document.getElementById('uploadForm').addEventListener('submit', function(event) {
    event.preventDefault();
    let formData = new FormData(this);
    fetch('/upload', {
        method: 'POST',
        body: formData
    })
    .then(response => {
        if (response.ok) {
            alert('File uploaded successfully!');
        } else {
            alert('Failed to upload file.');
        }
    })
    .catch(error => {
        console.error('Error:', error);
    });
});

function search() {
    const fileInput = document.getElementById('fileInput');
    const searchInput = document.getElementById('searchInput');
 
    if (!fileInput.files.length) {
        alert('Please upload a document first.');
        return;
    }
 
    const uploadedFile = fileInput.files[0];
    const question = searchInput.value;
 
    // Implement your search logic here
    // Assume searchResults is an array of objects with filenames and other information
    // let searchResults = [
    //     { filename: uploadedFile.name, content: `Answer to "${question}" for ${uploadedFile.name}` },
    //     // Add more results as needed
    // ];
   
 
    displayTextResults(searchResults);
    displayTableResults(searchResults);
}
 
function displayTextResults(results) {
    const textContainer = document.getElementById('text-container');
    textContainer.innerHTML = '';
 
    results.forEach(result => {
        const resultText = document.createElement('p');
        resultText.textContent = `${result.filename}: ${result.content}`;
        textContainer.appendChild(resultText);
    });
}
 
function displayTableResults(results) {
    const tableContainer = document.getElementById('table-container');
    const tableContent = document.getElementById('table-content');
    tableContent.innerHTML = '';
 
    if (results.length > 0) {
        // Create HTML table
        const table = document.createElement('table');
        table.classList.add('table-result');
        const headerRow = table.insertRow(0);
        const headers = ['Filename', 'Answer', 'Edit']; // Added 'Edit' header
 
        headers.forEach(header => {
            const th = document.createElement('th');
            th.textContent = header;
            headerRow.appendChild(th);
        });
 
        results.forEach(result => {
            const row = table.insertRow();
            const cell1 = row.insertCell(0);
            const cell2 = row.insertCell(1);
            const cell3 = row.insertCell(2); // Added cell for 'Edit'
 
            cell1.textContent = result.filename;
            cell2.textContent = result.content;
 
            // Create an edit icon and add it to the 'Edit' cell
            const editIcon = document.createElement('span');
            editIcon.className=" edit-icon";
            editIcon.innerHTML = '<i class="fas fa-edit"></i>';
            editIcon.addEventListener('click', () => openEditModal(result)); // Add click event for edit
            cell3.appendChild(editIcon);
 
            // Add more cells as needed
        });
 
        tableContent.appendChild(table);
        tableContainer.style.display = 'block';
    } else {
        tableContainer.style.display = 'none';
    }
}
 
// ... (unchanged parts) ...
 
function openEditModal(result) {
   
    const newContent = prompt(`Editing ${result.filename}. Enter new content:`, result.content);
   
    if (newContent !== null) {
        // User clicked OK
        result.content = newContent;
 
        // Find the index of the item in searchResults
        const index = searchResults.findIndex(item => item.filename === result.filename);
 
        // Update the actual searchResults array if the item is found
        if (index !== -1) {
            searchResults[index].content = newContent;
 
            // Update the displayed content
            displayTextResults(searchResults);
            displayTableResults(searchResults);
 
            console.log(`Updated content for ${result.filename}: ${result.content}`);
        } else {
            console.log(`Error: Item not found in searchResults array.`);
        }
    } else {
        // User clicked Cancel
        console.log(`Editing canceled for ${result.filename}`);
    }
}
 
 
 
// ... (unchanged parts) ...
 
 
 
 
function downloadCSV() {
   
    const results = searchResults;
     
    const csv = Papa.unparse(results);
   
    const blob = new Blob([csv], { type: 'text/csv;charset=utf-8;' });
    const link = document.createElement('a');
 
    if (navigator.msSaveBlob) { // IE 10+
        navigator.msSaveBlob(blob, 'search_results.csv');
    } else {
        link.href = URL.createObjectURL(blob);
        link.download = 'search_results.csv';
        link.style.display = 'none';
        document.body.appendChild(link);
        link.click();
        document.body.removeChild(link);
    }
}