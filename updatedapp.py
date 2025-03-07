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
if 'messages' not in st.session_state:
    st.session_state.messages = []

username = st.text_input("Enter your name:", key="name")
message = st.text_input("Type a message:", key="message")

# Max number of messages to display
MAX_MESSAGES = 20

# Send message to Firebase and update session state
if st.button("Send"):
    if username and message:
        ref = db.reference("/messages")
        ref.push({"user": username, "msg": message, "time": time.time()})

        # Refresh the messages after sending
        messages = ref.get()
        # Update session state messages
        if messages:
            st.session_state.messages = list(messages.values())
            # Keep only the most recent MAX_MESSAGES
            st.session_state.messages = st.session_state.messages[-MAX_MESSAGES:]

# Display messages from session state
st.subheader("Chat History:")
if st.session_state.messages:
    for msg in st.session_state.messages:
        st.write(f"**{msg['user']}**: {msg['msg']}")
else:
    st.write("No messages yet.")

# Refresh messages button
if st.button("Refresh Messages"):
    ref = db.reference("/messages")
    messages = ref.get()
    if messages:
        st.session_state.messages = list(messages.values())
        # Keep only the most recent MAX_MESSAGES
        st.session_state.messages = st.session_state.messages[-MAX_MESSAGES:]

# Add a note for users
st.write("Press 'Send' to submit your message or 'Refresh Messages' to see the latest messages.")
