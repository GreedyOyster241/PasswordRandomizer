import random
import streamlit as st
import pandas as pd

lower = "abcdefghijklmnopqrstuvwxyz"
upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
digits = "0123456789"
punctuation = "!@#$%^&*()_+-=[]{}|;:,.<>?"
addtopassword = ""
password = ""
session_state = st.session_state

if "saved_passwords" not in session_state:
    session_state.saved_passwords = []

st.title("Password Randomizer")
st.sidebar.header("Settings")
include_uppercase = st.sidebar.toggle("Include Uppercase", True)
include_lowercase = st.sidebar.toggle("Include Lowercase", True)
include_digits = st.sidebar.toggle("Include Digits", True)
include_punctuation = st.sidebar.toggle("Include Punctuation", True)
charlength = st.sidebar.slider("Character Length", 8, 32, 16)



if st.button("Generate Password"):
    if include_uppercase:
        addtopassword += upper
    if include_lowercase:
        addtopassword += lower
    if include_digits:
        addtopassword += digits
    if include_punctuation:
        addtopassword += punctuation
    if addtopassword:
        password = ""
        for i in range(charlength):
            random_char = random.choice(addtopassword)
            password += random_char

        st.session_state.saved_passwords.append(password)
        st.code(password)
        st.badge("Password generated successfully!", icon=":material/check:", color="green")


    else:
        st.badge("No characters selected. Please select at least one character type.", icon=":material/error:", color="red")


with st.sidebar.expander("Saved Passwords"):
    for password in st.session_state.saved_passwords:
        st.code(password)

clear_saved_passwords = st.sidebar.button("Clear Saved Passwords")
if clear_saved_passwords:
    st.session_state.saved_passwords = []
    st.sidebar.badge("Saved passwords cleared!", icon=":material/check:", color="green")
