import streamlit as st
from llm import main

st.set_page_config(page_title="Eid Mubarak Message Generator", page_icon="🌙")

st.markdown("""
    <style>
        body {
            background-color: #f8f9fa;
        }
        .stApp {
            background: linear-gradient(to right, #ff9a9e, #fad0c4);
            color: #333333;
        }
        .message-box {
            padding: 15px;
            background-color: #fff3cd;
            border-left: 5px solid #ff6f61;
            font-size: 20px;
            text-align: center;
            margin-top: 20px;
            border-radius: 10px;
            box-shadow: 0px 4px 6px rgba(0, 0, 0, 0.1);
        }
    </style>
""", unsafe_allow_html=True)

# Lists
tones = ["Formal", "Friendly", "Religious", "Poetic", "Spiritual","Casual"]
recipient_types = ["Family", "Friend", "Colleague", "Neighbor", "Boss"]

st.title("🌙 Eid Mubarak Message Generator")

# Inputs
tone = st.selectbox("Select a Tone", tones)
recipient_type = st.selectbox("Select Recipient Type", recipient_types)
recipient_name = st.text_input("Recipient Name")
sender_name = st.text_input("Your Name")

if st.button("Generate Message"):
    with st.status("Message is being written.....⏳", expanded=True) as status:
        message = main(tone, recipient_type,recipient_name,sender_name)
        st.markdown(f'<div class="message-box">{message}</div>', unsafe_allow_html=True)
  
