from flask import Flask, request, jsonify, render_template
from langchain_ollama import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate

# LangChain setup
template = """
Answer the question below.

Here is the conversation history: {context}

Question: {question}

Answer:
"""

model = OllamaLLM(model="llama3")
prompt = ChatPromptTemplate.from_template(template)
chain = prompt | model

# Flask app setup
app = Flask(__name__)

# Conversation context (to maintain state)
context = ""

@app.route("/")
def home():
    return render_template("index.html")  # Render the web page

@app.route("/chat", methods=["POST"])
def chat():
    global context
    user_input = request.json.get("message")  # Get user message from request
    if not user_input:
        return jsonify({"error": "No message provided"}), 400

    # Get response from LangChain
    result = chain.invoke({"context": context, "question": user_input})
    context += f"\nUser: {user_input}\nAI: {result}"  # Update context
    return jsonify({"response": result})

if __name__ == "__main__":
    app.run(debug=True)
