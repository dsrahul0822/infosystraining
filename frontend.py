import streamlit as st
from backend import chatmodel  # importing your existing backend model

st.set_page_config(page_title="Chatbot", layout="centered")

# ---------- WhatsApp UI CSS ----------
st.markdown("""
<style>
.chat-container {
    max-width: 700px;
    margin: auto;
    padding-bottom: 80px;
}

/* USER MESSAGE (Green bubble) */
.user-msg {
    background-color: #DCF8C6;
    color: #000000;   /* 🔥 FIX: Dark text */
    padding: 12px 16px;
    border-radius: 18px;
    margin: 10px 0;
    text-align: right;
    font-size: 16px;
    line-height: 1.5;
    font-family: "Segoe UI", sans-serif;
}

/* BOT MESSAGE (White bubble) */
.bot-msg {
    background-color: #FFFFFF;
    color: #000000;   /* 🔥 FIX: Dark text */
    padding: 12px 16px;
    border-radius: 18px;
    margin: 10px 0;
    text-align: left;
    font-size: 16px;
    line-height: 1.5;
    font-family: "Segoe UI", sans-serif;
    border: 1px solid #E5E5E5;
}

/* Chat input box */
textarea {
    font-size: 16px !important;
    color: #000000 !important;
}
</style>
""", unsafe_allow_html=True)


st.title("💬 Chatbot")

# ---------- Session State ----------
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# ---------- Chat Display ----------
st.markdown('<div class="chat-container">', unsafe_allow_html=True)

for msg in st.session_state.chat_history:
    if msg["role"] == "user":
        st.markdown(f'<div class="user-msg">{msg["content"]}</div>', unsafe_allow_html=True)
    else:
        st.markdown(f'<div class="bot-msg">{msg["content"]}</div>', unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)

# ---------- User Input ----------
user_input = st.chat_input("Type a message")

if user_input:
    # Add user message
    st.session_state.chat_history.append(
        {"role": "user", "content": user_input}
    )

    # Prepare prompt (same logic as backend)
    full_prompt = "\n".join(
        [
            f"User: {m['content']}" if m["role"] == "user" else f"AI: {m['content']}"
            for m in st.session_state.chat_history
        ]
    )

    # Model call
    response = chatmodel.invoke(full_prompt)

    # Add bot reply
    st.session_state.chat_history.append(
        {"role": "ai", "content": response.content}
    )

    st.rerun()
