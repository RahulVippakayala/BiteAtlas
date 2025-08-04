import streamlit as st
import requests
from datetime import datetime

# === Dify API Setup from Secrets ===
DIFY_API_KEY = st.secrets["DIFY_API_KEY"]
DIFY_BASE_URL = st.secrets.get("DIFY_BASE_URL", "https://api.dify.ai")  # optional override
DIFY_CHAT_ENDPOINT = f"{DIFY_BASE_URL}/v1/chat-messages"

# === Streamlit Page Setup ===
st.set_page_config(page_title="BiteAtlas", layout="wide")
st.image("biteatlas-logo.png", width=100)
st.markdown("## 🍛 **BiteAtlas – Ask About Foods, Places, and More**")

# === Sidebar with New Chat + History ===
st.sidebar.title("🧠 Chat History")

if "chat_sessions" not in st.session_state:
    st.session_state.chat_sessions = {}
if "current_session" not in st.session_state:
    st.session_state.current_session = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

# New chat button
if st.sidebar.button("➕ New Chat"):
    new_session_id = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    st.session_state.current_session = new_session_id

# Show previous sessions
for session_id in sorted(st.session_state.chat_sessions.keys(), reverse=True):
    label = "🟢 Current" if session_id == st.session_state.current_session else session_id
    if st.sidebar.button(label, key=session_id):
        st.session_state.current_session = session_id

# Ensure current session exists
if st.session_state.current_session not in st.session_state.chat_sessions:
    st.session_state.chat_sessions[st.session_state.current_session] = []

chat_history = st.session_state.chat_sessions[st.session_state.current_session]

# === Function to call Dify API ===
def ask_dify(message):
    try:
        headers = {
            "Authorization": f"Bearer {DIFY_API_KEY}",
            "Content-Type": "application/json"
        }
        payload = {
            "inputs": {},
            "query": message,
            "response_mode": "blocking",
            "user": "biteatlas-user"
        }
        response = requests.post(DIFY_CHAT_ENDPOINT, headers=headers, json=payload)
        response.raise_for_status()
        return response.json().get("answer", "🤖 No response received.")
    except requests.exceptions.RequestException as e:
        return f"❌ Error: {e}"

# === Display Chat ===
for msg in chat_history:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# === Input + Reply ===
query = st.chat_input("What do you want to explore today?")

if query:
    st.chat_message("user").markdown(query)
    chat_history.append({"role": "user", "content": query})

    reply = ask_dify(query)
    st.chat_message("assistant").markdown(reply)
    chat_history.append({"role": "assistant", "content": reply})
