import streamlit as st
from groq import Groq
from dotenv import load_dotenv
import os

# Load environment variables from the .env file
load_dotenv()

# Fetch the GROQ_API_KEY from the environment variables
GROQ_API_KEY = os.getenv('GROQ_API_KEY')

# Initialize the Groq client
client = Groq(api_key=GROQ_API_KEY)
MODEL = 'llama3-70b-8192'

def get_groq_response(question):
    messages = [
        {
            "role": "system",
            "content": "You are a chat bot designed only to answer questions related to Movies and Film industry. You do not know anything else. If someone asks questions on topics apart from Movies and Film industry, just say you don't know."
        },
        {
            "role": "user",
            "content": question,
        }
    ]

    response = client.chat.completions.create(
        model=MODEL,
        messages=messages,
        max_tokens=4096
    )

    return response.choices[0].message.content

# Streamlit app title
st.title("CineBot")

# Display an image placeholder
st.image("movies.webp", width=1000, caption="CinematicHub")

# Adjust CSS for padding and text wrapping
st.markdown("""
<style>
.block-container {
    padding-top: 3rem;  /* Adjust this value as needed */
    padding-bottom: 1rem; /* Ensure bottom content is visible */
    padding-left: 1rem;
    padding-right: 1rem;
}
.css-1r6slb0 {
    white-space: normal !important;
}
.sidebar-text {
    white-space: normal !important;
    word-wrap: break-word;
}
</style>
""", unsafe_allow_html=True)

# Input box for user query
query = st.text_input("Enter your query about movies:")

# Button to get response
if st.button("Search"):
    if query:
        # Get the response from the Groq model
        response = get_groq_response(query)
        # Display the response
        st.write("Response:", response)
    else:
        st.write("Please enter a query.")

# Additional Streamlit widgets for beautification
st.sidebar.header("About This App")
st.sidebar.markdown('<div class="sidebar-text">This app allows you to ask questions about the world of movies and the film industry. Feel free to explore and learn more about iconic films, legendary actors, and cinematic achievements!</div>', unsafe_allow_html=True)

# Add a footer
st.markdown("---")
st.markdown("Lights, camera, Streamlit! Built for film enthusiasts")
