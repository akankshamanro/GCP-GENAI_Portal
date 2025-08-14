document.addEventListener('DOMContentLoaded', () => {
    const sendButton = document.getElementById('send-button');
    const userInput = document.getElementById('user-input');
    const chatbox = document.getElementById('chat-box');
    const productContainer = document.querySelector('.product-container');

    // Initialize the conversation list
    const conversationList = [];

    sendButton.addEventListener('click', () => {
        const userQuestion = userInput.value; 

        if (!userQuestion) {
            return; // Do nothing if the input is empty
        }

        // Display the user's message in the chatbox
        addUserMessage(userQuestion);

        // Clear the user input field
        userInput.value = '';

        // Make a request to the Cloud Run API with userQuestion for chatbot response
        fetch('/stylemeqna', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ question: userQuestion}), // Include selected
        })
        .then(response => response.json())
        .then(data => {
            const answer = data.answer;

            // Display the bot's response in the chatbox
            addBotMessage(answer);

            // Add the conversation to the list
            conversationList.push({ 'User': userQuestion, 'Fashion Advisor': answer });
           
        })
        .catch(error => {
            console.error('Error fetching answer:', error);
        });
    });

});

const chatbox = document.getElementById('chat-box');

function addUserMessage(message) {
    const userContainer = document.createElement('div');
        userContainer.classList.add('message-container', 'user-container');
 
        const userMessageElement = document.createElement('div');
        userMessageElement.classList.add('message', 'user-message');
        userMessageElement.textContent = message;
        userContainer.appendChild(userMessageElement);
 
        const thinkingMessage = document.createElement('div');
        thinkingMessage.classList.add('message', 'bot-message', 'thinking');
        thinkingMessage.innerHTML = '<span class="material-symbols-outlined">smart_toy</span> Wait...';
        userContainer.appendChild(thinkingMessage);
 
        chatbox.appendChild(userContainer);
        chatbox.scrollTop = chatbox.scrollHeight;
}

// Function to add a bot message to the chatbox
function addBotMessage(message) {
    const userContainers = document.querySelectorAll('.user-container');
        const lastUserContainer = userContainers[userContainers.length - 1];
 
        const thinkingMessage = lastUserContainer.querySelector('.thinking');
        if (thinkingMessage) {
            lastUserContainer.removeChild(thinkingMessage);
        }
 
        const botMessageElement = document.createElement('div');
        botMessageElement.classList.add('message', 'bot-message');
        botMessageElement.innerHTML = `<span class="material-symbols-outlined">smart_toy</span> ${message}`;
        chatbox.appendChild(botMessageElement);
        chatbox.scrollTop = chatbox.scrollHeight;
}

const userInput = document.getElementById("user-input");
const sendButton = document.getElementById("send-button");

    // Listen for the "Enter" keypress event in the user input field
    userInput.addEventListener("keydown", function (event) {
        if (event.key === "Enter") {
            // Prevent the default "Enter" key behavior (e.g., line break)
            event.preventDefault();

            // Simulate a click on the send button
            sendButton.click();
        }
    });
