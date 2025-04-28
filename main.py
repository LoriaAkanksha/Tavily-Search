import streamlit as st
from tavily import TavilyClient

# Initialize TavilyClient with your API key
tavily = TavilyClient(api_key="tvly-1aGe3Ldzchi30zjXh87gBC5")

# Streamlit UI
st.title("Tavily Search")
query = st.text_input("Enter your query:")
if st.button("Search"):
    if query:
        response = tavily.search(query=query)
        st.write("Response:")
        st.write(response)
    else:
        st.warning("Please enter a query.")
