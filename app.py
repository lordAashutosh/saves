import streamlit as st
import firebase_admin
from firebase_admin import credentials, db
import time

# Function to initialize Firebase Admin SDK
def initialize_firebase():
    # Check if Firebase has already been initialized
    if not firebase_admin._apps:
        # Load Firebase credentials
        cred = credentials.Certificate(r"C:\Users\Public\streamlit-chat\streamlit-chat-ce69f-firebase-adminsdk-fbsvc-685d4d1957.json")  # Path to your downloaded JSON key
        firebase_admin.initialize_app(cred, {
            "databaseURL": "https://streamlit-chat-ce69f-default-rtdb.asia-southeast1.firebasedatabase.app/"  # Replace with your database URL
        })

# Initialize Firebase
initialize_firebase()

# Streamlit UI
st.title("🔵 Real-Time Chat")

# Input fields for username and message
username = st.text_input("Enter your name:", key="name")
message = st.text_input("Type a message:", key="message")

# Send message to Firebase
if st.button("Send"):
    if username and message:
        ref = db.reference("/messages")
        ref.push({"user": username, "msg": message, "time": time.time()})

# Display messages
st.subheader("Chat History:")
chat_ref = db.reference("/messages")
messages = chat_ref.get()

if messages:
    for msg in messages.values():
        st.write(f"**{msg['user']}**: {msg['msg']}")

# Add a button to refresh messages manually
if st.button("Refresh Messages"):
    st.experimental_rerun()  # This allows manual refresh

# Add a note for users
st.write("Press 'Send' to submit your message or 'Refresh Messages' to see the latest messages.")
