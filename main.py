import streamlit as st
from core.chatbot import GeminiChatBot
from core.memory import Memory

st.set_page_config(page_title="Gemini Chatbot", page_icon="🤖", layout="centered")

# Initialize session state
if "memory" not in st.session_state:
    st.session_state.memory = Memory()
if "bot" not in st.session_state:
    st.session_state.bot = GeminiChatBot()

st.title("🤖 Core2web Chatbot")
st.write("Chat with Google's Gemini model in real time!")

# Input field
user_input = st.chat_input("Type your message...")

if user_input:
    # Save user message
    st.session_state.memory.add("user", user_input)

    # Get response
    response = st.session_state.bot.chat(
        user_input, history=st.session_state.memory.get()
    )

    # Save bot response
    st.session_state.memory.add("model", response)

# Display chat history
for msg in st.session_state.memory.get():
    if msg["role"] == "user":
        with st.chat_message("user"):
            st.write(msg["parts"][0])
    else:
        with st.chat_message("assistant"):
            st.write(msg["parts"][0])
