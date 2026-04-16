import streamlit as st
import numpy as np
import pandas as pd

# ----------------------------
# Create a local "iris-like" dataset (no internet needed)
# ----------------------------
np.random.seed(42)

df = pd.DataFrame({
    "sepal_length": np.random.normal(5.8, 0.8, 150),
    "sepal_width": np.random.normal(3.0, 0.4, 150),
    "petal_length": np.random.normal(3.7, 1.7, 150),
    "petal_width": np.random.normal(1.2, 0.8, 150),
})

# ----------------------------
# App title
# ----------------------------
st.title("Hello Streamlit 👋")

# ----------------------------
# Dataset preview
# ----------------------------
st.subheader("Iris-like dataset (local)")
st.dataframe(df.head())

# ----------------------------
# Streamlit native chart (no matplotlib)
# ----------------------------
st.subheader("Feature distribution (line chart)")
st.line_chart(df)

# ----------------------------
# User inputs
# ----------------------------
st.subheader("Student Information")

student_name = st.text_input("Enter the student's name:")
student_age = st.slider("Select the student's age:", 1, 100)

if st.button("Display Information"):
    st.write(f"👤 Student's name: **{student_name}**")
    st.write(f"🎂 Student's age: **{student_age}**")
