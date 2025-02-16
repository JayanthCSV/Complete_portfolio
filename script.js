function toggleMenu() {
  const menu = document.querySelector(".menu-links");
  const icon = document.querySelector(".hamburger-icon");
  menu.classList.toggle("open");
  icon.classList.toggle("open");
}
function toggleChat() {
    const chatContainer = document.getElementById("chat-container");
    const chatbotIcon = document.getElementById("chatbot-icon");

    chatContainer.classList.toggle("hidden");

    // Stop floating animation when chat is opened
    if (!chatContainer.classList.contains("hidden")) {
        chatbotIcon.classList.add("stop-floating");
    } else {
        chatbotIcon.classList.remove("stop-floating");
    }
}

async function sendMessage() {
    let userInput = document.getElementById("user-input").value;
    if (!userInput) return;

    let messages = document.getElementById("messages");
    messages.innerHTML += `<div class="user-message">You: ${userInput}</div>`;

    document.getElementById("user-input").value = "";

    try {
        let response = await fetch("http://localhost:5000/chat", {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
            },
            body: JSON.stringify({ query: userInput }),
        });

        if (!response.ok) {
            throw new Error("Network response was not ok");
        }

        let data = await response.json();
        messages.innerHTML += `<div class="bot-message">Jay: ${data.answer}</div>`;
    } catch (error) {
        console.error("Fetch error:", error);
        messages.innerHTML += `<div class="message error">Error: Unable to fetch response.</div>`;
    }
}
