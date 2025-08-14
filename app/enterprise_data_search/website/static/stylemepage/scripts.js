document.addEventListener('DOMContentLoaded', () => {
    const sendButton = document.getElementById('send-btn');
    const userInput = document.getElementById('chat-input');
    const chatContainer = document.querySelector('.chat-container');
    const themeButton = document.getElementById('theme-btn');
    const deleteButton = document.getElementById('delete-btn');

    let userConversationId = null;
    let botConversationId = null;
    let conversationList = [];

    

    

    const generateUniqueId = () => {
        return Math.random().toString(36).substr(2, 9); // Example: "4nkf38w1"
    };

    
    const storeConversation = async (data, conversationType) => {
        const apiUrl = 'https://dev-gen-ai-service-retail-kcvokjzgdq-ew.a.run.app/store_conversation_data';
    
        try {
            const payload = {
                conversationId: data.role === 'user' ? userConversationId : botConversationId,
                userMessage: data.role === 'user' ? data.message : '',
                botMessage: data.role === 'bot' && conversationType !== 'likeDislike' ? data.message : '',
            };
    
            if (conversationType === 'likeDislike') {
                payload.like = data.like ? 1 : 0;
                payload.dislike = data.dislike ? 1 : 0;
            }
    
            await fetch(apiUrl, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify(payload),
            });
    
            console.log('Conversation stored successfully');
        } catch (error) {
            console.error('Error storing conversation:', error);
        }
    };
    
    
    
    

    
    // const loadDataFromLocalstorage = () => {
    //     const themeColor = localStorage.getItem('themeColor');
    //     document.body.classList.toggle('light-mode', themeColor === 'light_mode');
    //     themeButton.innerText = document.body.classList.contains("light-mode") ? "dark_mode" : "light_mode";
 
    //     chatContainer.innerHTML = localStorage.getItem("all-chats") || defaultText;
    //     conversationList = JSON.parse(localStorage.getItem('conversationList')) || [];
 
    //     displayConversation();
    // };

    const defaultText = `<div class="default-text">
    <h1>Rentokil Document Search</h1>
    <p>Start a conversation and explore the power of AI.</p>
    </div>`;
 
    const generateLikeDislikeId = () => {
        return `like_dislike_${generateUniqueId()}`;
    };
    
    

    const storeLikeDislike = async (action, conversationId) => {
        const apiUrl = 'https://dev-gen-ai-service-retail-kcvokjzgdq-ew.a.run.app/store_conversation_data';
    
        try {
            await fetch(apiUrl, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({
                    conversationId,
                    action,
                    conversationType: 'likeDislike',
                }),
            });
            console.log('Like/Dislike stored successfully');
        } catch (error) {
            console.error('Error storing like/dislike:', error);
        }
    };
    
    const handleLikeDislike = async (action, conversationId) => {
        const likeDislikeText = action === 'like' ? 'Liked!' : 'Disliked!';
        alert(likeDislikeText);
    
        // Make API call to store like/dislike
        await storeLikeDislike(action, conversationId);
    
        displayConversation(); // Update the conversation display
    };

    const displayConversation = () => {
        chatContainer.innerHTML = conversationList.length > 0
            ? ''
            : defaultText;

        conversationList.forEach((item) => {
            const { role, message, thinking, conversationId } = item;
            const messageElement = createMessageElement(role, message, thinking, conversationId);
            chatContainer.appendChild(messageElement);
        });

        chatContainer.scrollTop = chatContainer.scrollHeight;
    };

    const createMessageElement = (role, message, thinking, conversationId) => {
        const container = document.createElement('div');
        container.classList.add('chat', `${role}-chat`);

        const messageElement = document.createElement('div');
        messageElement.classList.add('message', `${role}-message`);

        const icon = role === 'bot' ? 'smart_toy' : 'face';
        messageElement.innerHTML = `<span class="material-symbols-rounded">${icon}</span> ${message}`;
        container.appendChild(messageElement);

        if (role === 'bot') {
            const copyBtn = createActionButton('content_copy', 'copy-btn', () => copyResponse(copyBtn));
            const likeBtn = createActionButton('thumb_up', 'like-btn', () => handleLikeDislike('like', conversationId));
            const dislikeBtn = createActionButton('thumb_down', 'dislike-btn', () => handleLikeDislike('dislike', conversationId));

            container.appendChild(copyBtn);
            container.appendChild(likeBtn);
            container.appendChild(dislikeBtn);
        }

        if (thinking) {
            const thinkingMessage = document.createElement('div');
            thinkingMessage.classList.add('message', 'bot-message', 'thinking');
            thinkingMessage.innerHTML = '<span class="material-symbols-rounded">smart_toy</span> Wait...';
            container.appendChild(thinkingMessage);
        }

        return container;
    };

    const createActionButton = (iconName, className, clickHandler) => {
        const actionBtn = document.createElement('span');
        actionBtn.classList.add('material-symbols-outlined', className);
        actionBtn.textContent = iconName;
        actionBtn.addEventListener('click', clickHandler);
        return actionBtn;
    };
    const copyResponse = (copyBtn) => {
        // Copy the text content of the response to the clipboard
        const responseTextElement = copyBtn.previousSibling; // Assuming the <p> element is a sibling of the copy button
        navigator.clipboard.writeText(responseTextElement.textContent);
        copyBtn.textContent = 'done';
        setTimeout(() => (copyBtn.textContent = 'content_copy'), 1000);
    };


    

    

    // Modify your existing addBotMessage and addUserMessage functions
    const addUserMessage = async (message) => {
        // Generate a new user conversation ID
        userConversationId = generateUniqueId();

        conversationList.push({ role: 'user', message, conversationId: userConversationId });
        displayConversation();

        // Make API call to store the user message
        await storeConversation({ role: 'user', message });
    };

    const addBotMessage = async (message, thinking = false) => {
        // Generate a new bot conversation ID
        botConversationId = generateUniqueId();

        let content;

        if (isTabularFormat(message)) {
            content = convertTabularToHTMLTable(message);
        } else {
            content = message;
        }

        conversationList.push({ role: 'bot', message: content, thinking, conversationId: botConversationId });
        displayConversation();

        // Make API call to store the bot message
        await storeConversation({ role: 'bot', message: content, thinking });
    };
    
    
    
 
    
    

     
    const isTabularFormat = (text) => {
        // Check if the text has a structure resembling a table (e.g., contains | and ---)
        return /\|.*\|.*\|/.test(text) && /\|.*\|/.test(text);
    };
     
    const convertTabularToHTMLTable = (tabularData) => {
        // Split the tabular data into rows
        const rows = tabularData.trim().split(/\n/);
        
        // Filter out rows containing "---"    
        const filteredRows = rows.filter(row => !/---/.test(row));
        // Create an HTML table
        const table = document.createElement('table');
        table.classList.add('custom-table'); // Add a custom class for styling
     
        // Create table body
        const tbody = document.createElement('tbody');
     
        filteredRows.forEach((row, rowIndex) => {
            // Split each row into cells
            const cells = row.split('|').filter(Boolean).map(cell => cell.trim());
     
            // Create a table row
            const tr = document.createElement('tr');
            tr.classList.add(rowIndex % 2 === 0 ? 'even-row' : 'odd-row'); // Alternating row colors
     
            cells.forEach((cell, cellIndex) => {
                // Create a table cell
                const td = document.createElement('td');
                td.textContent = cell;
     
                // Add custom styles based on cell or row index
                if (rowIndex === 0) {
                    // Header row styles
                    td.classList.add('header-cell');
                } else {
                    // Data row styles
                    td.classList.add(cellIndex % 2 === 0 ? 'even-cell' : 'odd-cell'); // Alternating cell colors
                }
     
                // Append the cell to the row
                tr.appendChild(td);
            });
     
            // Append the row to the table body
            tbody.appendChild(tr);
        });
     
        // Append the table body to the table
        table.appendChild(tbody);
     
        return table.outerHTML;
    };
 
    const handleOutgoingChat = () => {
        const userQuestion = userInput.value.trim();
 
        if (!userQuestion) {
            return; // Do nothing if the input is empty
        }
 
        addUserMessage(userQuestion);
 
        userInput.value = ''; // Clear the user input field
 
        // Make a request to the Cloud Run API with userQuestion for chatbot response
        fetch('/stylemeqna', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ question: userQuestion }),
        })
            .then((response) => response.json())
            .then((data) => {
                const answer = data.answer;
                addBotMessage(answer);
            })
            .catch((error) => {
                console.error('Error fetching answer:', error);
            });
    };
 
    sendButton.addEventListener('click', handleOutgoingChat);
 
    userInput.addEventListener('keydown', (event) => {
        if (event.key === 'Enter') {
            event.preventDefault();
            handleOutgoingChat();
        }
    });
 
    deleteButton.addEventListener('click', () => {
        if (confirm('Are you sure you want to delete all the chats?')) {
            localStorage.removeItem('conversationList');
            loadDataFromLocalstorage();
        }
    });
 
    // themeButton.addEventListener('click', () => {
    //     document.body.classList.toggle('light-mode');
    //     const themeColor = document.body.classList.contains('light-mode') ? 'light_mode' : 'dark_mode';
    //     localStorage.setItem('themeColor', themeColor);
    // });
 
    
});