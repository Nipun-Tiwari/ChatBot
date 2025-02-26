# frontend.py
import streamlit as st
import requests
import matplotlib.pyplot as plt
import seaborn as sns

st.title("Titanic Dataset Chatbot 🚢")

# Input for user question
question = st.text_input("Ask a question about the Titanic dataset:")

if question:
    # Send the question to the backend
    response = requests.get(f"http://127.0.0.1:8000/query?question={question}").json()
    
    # Display the response
    if "histogram" in response["response"]:
        st.write("Here's a histogram of passenger ages:")
        ages = response["data"]
        fig, ax = plt.subplots()
        sns.histplot(ages, bins=20, kde=True, ax=ax)
        st.pyplot(fig)
    else:
        st.write(response["response"])