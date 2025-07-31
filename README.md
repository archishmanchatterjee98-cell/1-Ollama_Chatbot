# 1-Ollama_Chatbot

Intro: 
A lightweight, customizable chatbot built with Ollama for running large language models (LLMs) locally — no cloud dependency, no API keys.

🔍 Features
🦙 Uses local models like llama2, mistral, etc. via Ollama

💬 Supports multi-turn conversations with chat history

🧱 Built with LangChain and Streamlit for modularity and fast UI


⚡ Fast inference with minimal system resources

🚀 Tech Stack
Ollama — local LLM runtime

LangChain — LLM orchestration

Streamlit — UI framework

Python 3.13+

📦 Use Cases
Offline AI assistant

Local coding helper

Lightweight developer tool


Prerequisites
Before running this application, ensure the following:

Python 3.8+ is installed on your machine.

Install required packages via pip:

bash
Copy
Edit
pip install streamlit langchain langchain-community python-dotenv
Ollama must be installed and running locally
Refer to https://ollama.com for installation instructions.

Models like llama2, gemma2, or mistral should be available locally in Ollama.
You can pull them using:

bash
Copy
Edit
ollama pull llama2
ollama pull gemma2
ollama pull mistral
.env file (optional but recommended):
You may create a .env file in the root directory to manage environment variables (e.g., for future enhancements like API keys or configuration).




