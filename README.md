# Open Source Portfolio Project with AI Chatbot

**A modular web portfolio with integrated AI chatbot** designed for students and developers to showcase skills while learning modern full-stack development. Built with Flask, LangChain, and responsive CSS.

## Project Structure

portfolio-project/

├── static/

│ ├── css/

│ │ └── style.css # Responsive styling & chatbot UI

│ └── js/

│ └── script.js # Chat interactions & animations

├── templates/

│ └── index.html # Main portfolio content

├── app.py # Flask backend & AI integration

├── assets/

│ └── chatbot_data.pdf # Your resume/CV data

├── requirements.txt # Python dependencies
├── requirements.txt # Python dependencies

## Key Features

**🤖 Smart Resume Chatbot**
- Answers questions using your resume data through RAG architecture
- Casual conversational style (`app.py` lines 28-32)
- Context-aware responses under 50 words

**🎨 Modern UI Components**
- Floating chatbot icon with animation (`style.css` lines 314-339)
- Responsive hamburger menu (`script.js` lines 1-21)
- Project cards with hover effects

**🔧 Easy Customization**
To modify chatbot personality (app.py)

prompt = ChatPromptTemplate.from_template("""
Act like a [YOUR_ROLE] searching for [JOB_TYPE].
Keep responses under 50 words.
{context}
Question: {input}
""")

## Setup Guide

1. **Install dependencies**

pip install -r requirements.txt

2. **Configure API keys**
In app.py

os.environ["GROQ_API_KEY"] = "your_api_key_here"


3. **Add your resume**
- Replace `assets/chatbot_data.pdf` with your resume
- The AI will automatically process it[

4. **Run development server**

flask run --host=0.0.0.0 --port=5000

## Customization Options

**UI Themes**

/* Change color scheme in style.css /
:root {
--primary-color: #2A2A2A; / Dark gray /
--accent-color: #4CAF50; / Green /
--chatbot-bg: #FFFFFF; / White background */
}

**Chatbot Features**

// Add new UI interactions in script.js
function toggleDarkMode() {
document.body.classList.toggle("dark-theme");
}


## Contributing

We welcome contributions! Please follow our guidelines:

1. Fork the repository
2. Create feature branch (`git checkout -b feature/amazing-feature`)
3. Commit changes (`git commit -m 'Add amazing feature'`)
4. Push to branch (`git push origin feature/amazing-feature`)
5. Open Pull Request

**Report issues** for:
- Broken links
- Responsive design bugs
- Chatbot response errors

## Learning Resources

- [Open Source Best Practices](https://opensauced.pizza)
- [LangChain Documentation](https://python.langchain.com)

**Built with:**
- Flask (Python backend)
- LangChain (AI integration)
- HuggingFace (NLP models)
- Groq (LLM API)


