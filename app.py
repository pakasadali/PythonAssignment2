import streamlit as st
import random

st.set_page_config(page_title="Number Guessing Game", layout="wide")

st.title("Number Guessing game 🔢")

st.subheader("Guess a number between 1 to 100 ")

if "random_number" not in st.session_state:
    st.session_state.random_number = random.randint(1,100)
    st.session_state.attempts = 0

st.write("Enter number here")

userInput = st.text_input("Enter number")


if userInput:
    _number = int(userInput)
    st.session_state.attempts += 1
    
    if _number ==  st.session_state.random_number:
        st.markdown(f"<h2>You are correct the number is  : { st.session_state.random_number} </h2>", unsafe_allow_html=True)
        st.markdown(f"<h4>Your guessed it in  : { st.session_state.attempts} attempts</h4>", unsafe_allow_html=True)
    elif _number >  st.session_state.random_number:
        st.markdown(f"<h2>Too High</h2>", unsafe_allow_html=True)
    elif _number <  st.session_state.random_number:
        st.markdown(f"<h2>Too Low</h2>", unsafe_allow_html=True)

    st.write(f"Attempts : {st.session_state.attempts}")