import streamlit as st
import random
st.title("Number Guessing Game")
if "random_number" not in st.session_state:
    st.session_state["random_number"] = random.randint(1, 100)

if "attempts" not in st.session_state:
    st.session_state["attempts"] = 0


guess = st.number_input("Guess a number between 1 and 100:", min_value=1, max_value=100, step=1, key="guess_number")

st.status(f"are u ready for testing ur unholy luck", expanded=False, state="complete")
if st.button("try ur luck, idoit"):
    st.session_state["attempts"] += 1
    if guess < st.session_state["random_number"]:
        st.warning(" damn idoit , it's too low ==>Try again.")
    elif guess > st.session_state["random_number"]:
        st.warning(" damn idoit ,it's too high ==>Try again.")
    else:
        st.success(f"Congratulations idoit ! You guessed the number in {st.session_state['attempts']} attempts.")
        
        if st.button("Play Again"):
            st.session_state["random_number"] = random.randint(1, 100)
            st.session_state["attempts"] = 0
