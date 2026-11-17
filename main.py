import os
from datetime import datetime
import streamlit as st
from dotenv import load_dotenv
from google import genai
from google.genai import types

load_dotenv()

API_KEY = os.getenv("GEMINI_API_KEY")
if not API_KEY:
    st.error("CRITICAL ERROR: GEMINI_API_KEY missing in environment variables!")
    st.stop()

client = genai.Client(api_key=API_KEY)

st.set_page_config(page_title="AI Research Chat", page_icon="🤖", layout="centered")

st.title("🤖 AI Research Chat Agent")
st.markdown("Your persistent research assistant powered by Gemini 3.5 Flash-Lite.")

LOG_FILENAME = "research_logs.txt"

def save_log(prompt: str, response: str, filename: str = LOG_FILENAME):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_entry = f"""==================================================
Timestamp: {timestamp}
PROMPT:
{prompt}

RESPONSE:
{response}
==================================================\n\n"""
    with open(filename, "a", encoding="utf-8") as f:
        f.write(log_entry)

# --- Sidebar per la gestione dei log ---
with st.sidebar:
    st.header("⚙️ Research Management")
    st.markdown("Download your session research logs below.")
    
    if os.path.exists(LOG_FILENAME):
        with open(LOG_FILENAME, "r", encoding="utf-8") as f:
            log_data = f.read()
        
        st.download_button(
            label="📥 Download Research Logs",
            data=log_data,
            file_name=LOG_FILENAME,
            mime="text/plain"
        )
    else:
        st.info("No logs generated in this session yet.")

if "chat_session" not in st.session_state:
    st.session_state.chat_session = client.chats.create(
        model='gemini-3.5-flash-lite',
        config=types.GenerateContentConfig(
            temperature=0.7,
            system_instruction="You are a brilliant, concise, and helpful assistant. You remember the full context of the conversation."
        )
    )

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if user_prompt := st.chat_input("Type your question here..."):
    st.session_state.messages.append({"role": "user", "content": user_prompt})
    with st.chat_message("user"):
        st.markdown(user_prompt)

    with st.chat_message("assistant"):
        with st.spinner("Processing..."):
            try:
                response = st.session_state.chat_session.send_message(user_prompt)
                response_text = response.text
                st.markdown(response_text)
                st.session_state.messages.append({"role": "assistant", "content": response_text})
                save_log(user_prompt, response_text)
            except Exception as e:
                error_message = f"Error: {e}"
                st.error(error_message)
