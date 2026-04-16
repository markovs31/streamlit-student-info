import streamlit as st
import numpy as np

# Import your libraries here
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns




# Load the iris dataset
df = sns.load_dataset('iris')

# Violin plot for every feature
sns.violinplot(data=df)
fig = plt.gcf();


# Title of the app
st.title("Hello Streamlit 👋")



student_name = st.text_input("Enter the student's name:", icon="🚨")
# Slider for student's age
student_age = st.slider("Select the student's age:", 1, 100)
# Button to display the input text and age
if st.button("Display Information"):
    st.write("Student's name: ",student_name)
    st.write("Student's age: ",student_age)