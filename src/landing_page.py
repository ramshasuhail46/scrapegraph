import streamlit as st

# Check if the user is logged in
def check_login_and_redirect(page):
    """Function to check if user is logged in and reroute to the respective page"""
    if st.session_state.logged_in:
        st.switch_page(page)  # Rerun the app to the respective page if logged in
    else:
        st.session_state.show_signup = False  # Ensure user is redirected to login
        st.error("Please log in to access this page.")
        st.switch_page("pages/login.py")  


def display_landing_page():
    """Display the landing page with descriptions and buttons to redirect to each tool"""

    # Set the title of the landing page
    st.title("Welcome to the Data Insights Platform")

    st.write("""
    This platform provides several tools to help you analyze data, create scripts, and generate visual insights.
    Each tool is described below:
    """)

    # Display each component in its own box with description and a button to navigate
    with st.expander("📜 Script Creator Graph"):
        st.write("""
        The **Script Creator Graph** allows you to Single-page scraper that extracts information from a website and generates a Python script.
        """)
        if st.button("Go to Script Creator"):
            check_login_and_redirect("pages/ScriptCreatorGraph.py")

    with st.expander("📜 Script Creator Multi Graph"):
        st.write("""
        The **Script Creator Multi Graph** enables Multi-page scraper that generates a Python script for extracting information from multiple pages and sources.
        """)
        if st.button("Go to Script Creator Multi"):
            check_login_and_redirect("pages/ScriptCreatorMultiGraph.py")

    with st.expander("🔍 Search Graph"):
        st.write("""
        The **Search Graph** extracts information from the top n search results of a search engine.""")
        if st.button("Go to Search Graph"):
            check_login_and_redirect("pages/SearchGraph.py")

    with st.expander("📊 Smart Graph"):
        st.write("""
        The **Smart Graph** tool uses advanced algorithms to scrape a single-page that only needs a user prompt and an input source.
        """)
        if st.button("Go to Smart Graph"):
            check_login_and_redirect("pages/SmartScraperGraph.py")

    with st.expander("📊 Smart Graph Multi"):
        st.write("""
        **Smart Graph Multi** extends the capabilities of the Smart Graph by extracting information from multiple pages given a single prompt and a list of sources.
        """)
        if st.button("Go to Smart Graph Multi"):
            check_login_and_redirect("pages/SmartScraperMultiGraph.py")


    with st.expander("📊 Speech Graph"):
        st.write("""
        **Speech Graph** extends the capabilities by extracting information from a website and generates an audio file.

        """)
        if st.button("Go to Speech Graph"):
            check_login_and_redirect("pages/SpeechGraph.py")

