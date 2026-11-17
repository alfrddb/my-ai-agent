import os
from datetime import datetime
import streamlit as st
from dotenv import load_dotenv
from google import genai
from google.genai import types

load_dotenv()

API_KEY = os.getenv("GEMINI_API_KEY") or st.secrets.get("GEMINI_API_KEY")
if not API_KEY:
    st.error("CRITICAL ERROR: GEMINI_API_KEY missing in environment variables or Streamlit secrets!")
    st.stop()

st.set_page_config(page_title="AI Research Chat", page_icon="🤖", layout="centered")

st.title("🤖 AI Research Chat Agent")
st.markdown("Your persistent research assistant powered by Gemini 3.5 Flash-Lite.")

@st.cache_resource
def get_genai_client(api_key: str):
    return genai.Client(api_key=api_key)

client = get_genai_client(API_KEY)

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
            except Exception as e:
                error_message = f"Error: {e}"
                st.error(error_message)

with st.sidebar:
    st.header("⚙️ Research Management")
    st.markdown("Download your current session logs anytime.")
    
    if st.session_state.messages:
        log_content = f"AI Research Chat Session Export - {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n"
        log_content += "=" * 50 + "\n\n"
        
        for msg in st.session_state.messages:
            role = "USER" if msg["role"] == "user" else "ASSISTANT"
            log_content += f"[{role}]:\n{msg['content']}\n\n" + "-" * 30 + "\n\n"
            
        st.download_button(
            label="📥 Download Session Log",
            data=log_content.encode("utf-8"),
            file_name="research_log.txt",
            mime="text/plain"
        )
    else:
        st.info("Start chatting to generate downloadable logs.")
