import streamlit as st
import joblib

# Load model and vectorizer
model = joblib.load("sentiment_model.pkl")
vectorizer = joblib.load("vectorizer.pkl")

st.title("Sentiment Analysis of Amazon Food Reviews")
st.write("Enter a customer review below to analyze its sentiment.")

user_input = st.text_area("Customer Review")

if st.button("Predict Sentiment"):
    clean_text = user_input.lower()
    clean_text = ''.join([char for char in clean_text if char.isalnum() or char.isspace()])
    vectorized_input = vectorizer.transform([clean_text])
    prediction = model.predict(vectorized_input)[0]
    sentiment = "Positive 😊" if prediction == 1 else "Negative 😞"
    st.success(f"Predicted Sentiment: {sentiment}")
