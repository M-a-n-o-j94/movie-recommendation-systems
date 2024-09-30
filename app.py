import streamlit as st
from langchain import PromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI
import google.generativeai as genai
from dotenv import load_dotenv  # For API key storing
import os

# Load environment variables
load_dotenv()
genai.configure(api_key=os.getenv("Manoj-Api-Key"))

# Streamlit app layout
st.title("Movie Recommender System")
user_input = st.text_input("Enter the Movie Title, Genre, or Keyword:")

# Create a prompt template
demo_template = '''Give me movie recommendations for the following genre or keyword: {prompt}'''
template = PromptTemplate(
    input_variables=['prompt'],
    template=demo_template
)

# Initialize Google Gemini model
llm = ChatGoogleGenerativeAI(model="gemini-pro", api_key=os.getenv("Manoj-Api-Key"))

if user_input:
    prompt = template.format(prompt=user_input)
    recommendations = llm.predict(text=prompt)
    st.write(f"Recommendations for you:\n{recommendations}")
else:
    st.write('Please enter a movie title, genre, or keyword to get recommendations.')
