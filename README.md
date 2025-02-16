### Portfolio Website

# 🤖 AI-Powered Portfolio Website with Interactive Chatbot 

![Project Demo](https://via.placeholder.com/800x400.png?text=Portfolio+Chatbot+Demo)  
*(Replace with your actual demo GIF/video)*

A smart portfolio website that lets visitors chat with an AI version of you! Perfect for students/job seekers to showcase skills and handle FAQs through an intelligent chatbot.

## 🌈 Key Features
- **Interactive Portfolio** with projects/experience sections  
- **AI Twin Chatbot** trained on your resume (PDF)  
- **Floating Chat Interface** with animations  
- **RAG System** for accurate resume-based answers  
- **Mobile Responsive** design  

## 🧩 Project Structure
portfolio-chatbot/
├── app.py # Flask backend & AI logic
├── script.js # Chat interactions & animations
├── style.css # All styling rules
├── index.html # Main portfolio content
├── assets/
│ └── chatbot_data.pdf # Your resume (add yours!)
├── requirements.txt # Python dependencies
└── .env # API keys (not committed)

text

## 🚀 Quick Start

### 1. Clone & Setup
git clone https://github.com/yourusername/portfolio-chatbot.git
cd portfolio-chatbot
pip install -r requirements.txt

text

### 2. Add Your Resume
1. Save your resume as `assets/chatbot_data.pdf`  
2. Get [Groq API key](https://console.groq.com/)  
3. Create `.env` file:
GROQ_API_KEY="your-api-key-here"

text

### 3. Launch!
flask run --port 5000

text
Open `http://localhost:5000` in your browser.

## 🛠️ Core Components Explained

### 🤖 AI Backend (`app.py`)
Load and process resume
resume_loader = PyPDFLoader("assets\chatbot_data.pdf")
docs = resume_loader.load()

Create AI personality
prompt = ChatPromptTemplate.from_template("""
Act like the resume owner - be enthusiastic, casual, and keep answers under 50 words!
{context}
Question: {input}
""")

Build RAG system
retriever = vectors.as_retriever()
document_chain = create_stuff_documents_chain(llm, prompt)
retrieval_chain = create_retrieval_chain(retriever, document_chain)

text

### 💬 Chat Interface (`script.js`)
async function sendMessage() {
let userInput = document.getElementById("user-input").value;

// Show user message
messages.innerHTML += <div class="user-message">${userInput}</div>;

// Get AI response
let response = await fetch("http://localhost:5000/chat", {
method: "POST",
headers: { "Content-Type": "application/json" },
body: JSON.stringify({ query: userInput })
});

// Display bot response
let data = await response.json();
messages.innerHTML += <div class="bot-message">${data.answer}</div>;
}

text

### 🎨 Styling Tricks (`style.css`)
/* Floating animation */
#chatbot-icon {
animation: floatUpDown 2s infinite ease-in-out;
}

@keyframes floatUpDown {
0%, 100% { transform: translateY(0); }
50% { transform: translateY(-10px); }
}

/* Chat message bubbles */
.user-message {
background: #d1e7dd;
border-radius: 15px 15px 0 15px;
}

.bot-message {
background: #f0f0f0;
border-radius: 15px 15px 15px 0;
}

text

## 🧑💻 Customization Guide

### 1. Update Portfolio Content
Edit **index.html** sections:
<!-- About Section --> <section id="about"> <h1 class="title">Data Scientist</h1> <div class="section-container"> <!-- Update your bio here --> <p>When I’m not crushing it in the gym, I’m crushing complex data problems...</p> </div> </section> ```
2. Modify Chatbot Personality
Adjust the AI's tone in app.py:

text
# Current personality settings
prompt = ChatPromptTemplate.from_template("""
Act enthusiastic! Use student slang when appropriate.
Keep answers under 3 sentences. Add emojis occasionally 😊

{context}
Question: {input}
""")
3. Add New Features
Example: Add Dark Mode

Add toggle button in index.html:

text
<button id="dark-mode-toggle" class="btn">🌓 Toggle Dark Mode</button>
Add JavaScript in script.js:

text
document.getElementById('dark-mode-toggle').addEventListener('click', () => {
  document.body.classList.toggle('dark-mode');
});
Style in style.css:

text
.dark-mode {
  background-color: #1a1a1a;
  color: white;
}
🐛 Common Issues & Fixes
Issue	Solution
Chat not responding	Check Flask server is running on port 5000
API errors	Verify .env file has valid Groq API key
Styling broken	Clear browser cache + reload
PDF not loading	Ensure resume is in /assets as chatbot_data.pdf
🤝 Contributing
Want to improve this project?

Fork the repository

Create a feature branch (git checkout -b cool-feature)

Commit changes (git commit -m 'Add awesome feature')

Push to branch (git push origin cool-feature)

Open a Pull Request
