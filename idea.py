import streamlit as st
import requests

# Replace with your API key and endpoint
API_KEY = "your_api_key_here"
SEARCH_ENGINE_ID = "your_search_engine_id_here"
API_ENDPOINT = f"https://www.googleapis.com/customsearch/v1"

def search_query(query):
    """Search the query using an API and return recommended links."""
    try:
        params = {
            'q': query,
            'key': API_KEY,
            'cx': SEARCH_ENGINE_ID
        }
        response = requests.get(API_ENDPOINT, params=params)
        response.raise_for_status()
        results = response.json()
        links = []

        # Extract titles and links from the search results
        if "items" in results:
            for item in results["items"]:
                links.append((item["title"], item["link"]))
        return links

    except Exception as e:
        st.error(f"Error fetching results: {e}")
        return []

# Streamlit app
st.title("Search the Internet")

# Input query from user
query = st.text_input("Enter your query below:")

if st.button("Search"):
    if query.strip():
        st.write(f"Searching for: **{query}**")
        results = search_query(query)

        if results:
            st.write("### Recommended Websites:")
            for title, link in results:
                st.write(f"- [{title}]({link})")
        else:
            st.write("No results found. Try refining your query.")
    else:
        st.error("Please enter a valid query.")

st.write("Powered by Google Custom Search API")
