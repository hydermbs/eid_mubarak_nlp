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
        input, select {
            background-color: white !important;
            color: black !important;
            border: 1px solid #ccc !important;
            border-radius: 5px !important;
            padding: 10px !important;
        }
        select {
            background-color: white !important;
            color: black !important;
            border: 1px solid #ff6f61 !important;
            padding: 10px !important;
            border-radius: 5px !important;
        }
        button {
            background-color: white !important;
            color: black !important;
            border: 2px solid #ff6f61 !important;
            border-radius: 5px !important;
            padding: 10px 20px !important;
            font-size: 16px !important;
            cursor: pointer !important;
        }
        button:hover {
            background-color: #ff6f61 !important;
            color: white !important;
        }
    </style>
""", unsafe_allow_html=True)

# Lists
tones = ["Formal", "Friendly", "Religious"]
recipient_types = ["Family", "Friend", "Colleague", "Neighbor"]

st.title("🌙 Eid Mubarak Message Generator")

# Inputs
tone = st.selectbox("Select a Tone", tones)
recipient_type = st.selectbox("Select Recipient Type", recipient_types)
recipient_name = st.text_input("Recipient Name")
sender_name = st.text_input("Your Name")

if st.button("Generate Message"):
    if recipient_name and sender_name:
        message = main(tone, recipient_type,recipient_name,sender_name)
        st.markdown(f'<div class="message-box">{message}</div>', unsafe_allow_html=True)
    else:
        st.warning("Please enter both recipient and sender names.")
