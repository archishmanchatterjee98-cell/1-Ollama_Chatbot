import os
from dotenv import load_dotenv
import streamlit as st
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_community.llms import Ollama

# Load env vars and set tracing
load_dotenv()
os.environ["LANGCHAIN_TRACING_V2"] = "true"
os.environ["LANGCHAIN_PROJECT"] = "Q&A Chatbot With OLLAMA"
os.environ["LANGCHAIN_API_KEY"] = os.getenv("LANGCHAIN_API_KEY")

DEFAULT_ASSISTANT_MSG = "Hi! I am a helpful assistant. How can I help you?"
# Prompt template
prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful assistant. Please respond to the user's questions accurately and concisely."),
    ("user", "Question: {question}"),
])

# Generate response
def generate_response(question, llm, temperature):
    model = Ollama(model=llm, temperature=temperature)
    chain = prompt | model | StrOutputParser()
    return chain.invoke({"question": question})

# Initialize session
def initialize_session():
    return [{"role": "assistant", "content": DEFAULT_ASSISTANT_MSG}]



# Streamlit UI
st.title("🧠 Q&A Chatbot with Ollama")
st.caption("Go Ahead and ask your question!")

# Sidebar
with st.sidebar:
    st.header("⚙️ Settings")
    llm = st.selectbox("Model", ["llama2", "gemma2", "mistral"], index=0)
    temperature = st.slider("Temperature", min_value=0.0, max_value=1.0, value=0.7)
    max_tokens = st.number_input("Max Tokens", min_value=50, max_value=300, value=150)

    if st.button("🧹 Clear Chat"):
        st.session_state.messages = initialize_session()
        st.rerun()

# Setup message history
if "messages" not in st.session_state:
    st.session_state.messages = initialize_session()

# Display chat
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])

# Handle user input
if question := st.chat_input("Ask me anything !!"):
    st.session_state.messages.append({"role": "user", "content": question})
    with st.chat_message("user"):
        st.write(question)

    response = generate_response(question, llm, temperature)
    st.session_state.messages.append({"role": "assistant", "content": response})

    with st.chat_message("assistant"):
        st.write(response)

        