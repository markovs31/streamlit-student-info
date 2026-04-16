import streamlit as st
# Title of the app
st.title("Hello Streamlit 👋")
student_name = st.text_input("Enter the student's name:", icon="🚨")
# Slider for student's age
student_age = st.slider("Select the student's age:", 1, 100)
# Button to display the input text and age
if st.button("Display Information"):
    st.write("Student's name: ",student_name)
    st.write("Student's age: ",student_age)