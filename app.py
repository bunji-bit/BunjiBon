import streamlit as st

# Title of the app
st.title("✨ My First Streamlit App")

# Add some text
st.write("Hello, world! This is my first Streamlit app. 🎉")

# Input box
name = st.text_input("What's your name?")

# Button
if st.button("Say hi 👋"):
    st.success(f"Hey {name}, welcome to Streamlit! 🌈")
