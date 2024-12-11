## 🌟 Flask Chatbot with LangChain & Ollama 🌟
This project is a Flask-based chatbot powered by LangChain and Ollama LLM that allows users to interact with AI-powered responses through a web interface. 🚀

# ✨ Features
- 🗣️ Chat Interface: Users can send messages, and the chatbot responds with context-aware AI-powered answers.
- 🔗 Flask App: A simple web app built using Flask for serving the chatbot.
- 🔍 LangChain: Handles context-aware chat by maintaining conversation history.
- 🤖 Ollama LLM: AI model used for generating accurate and context-based responses.
  
# 📋 Prerequisites
  Before you begin, ensure you have the following installed:
  1. 💻 Python (v3.8 or higher)
  2. 📦 Flask: Install using pip install flask
  3. 🌐 LangChain Ollama: Install using pip install langchain_ollama
     
# ⚙️ Setup Instructions
**Clone the repository:**

```bash
git clone https://github.com/yourusername/llama-bot.git
cd llama-bot
```
**Set up a virtual environment:**

```bash
python -m venv venv  # Create a virtual environment
source venv/bin/activate  # Activate the virtual environment
```
**Install project dependencies:**

```bash
pip install flask langchain langchain_ollama
```
**Run the Flask app:**

```bash
python main.py
```

# Access the chatbot:
Open your browser and go to http://localhost:5000 to interact with the chatbot.

📂 Folder Structure
bash
Copy code
llama-bot/
│
├── chatbot/                  # Virtual environment (do not push this to Git)
├── .gitignore              # Configuration to ignore sensitive files like .env
├── main.py                 # Flask app entry point
├── templates/              # HTML templates (e.g., index.html for chat interface)
└── README.md               # This README file

# 🛠️ How It Works
Home Page:
The chatbot interface is served via index.html and renders the chat UI.

# Chat Endpoint (/chat):

- Accepts user messages via POST request.
- Uses LangChain to generate AI-powered responses based on the conversation history.
- Maintains context to keep track of previous user queries.
  
# Context-Aware Responses:
- Every new message updates the conversation context, ensuring contextually relevant responses.


# 🎉 Happy Chatting!
Feel free to contribute, suggest, or give a star ⭐ on GitHub! 😊
