import streamlit as st
from db import create_tables, get_db_connection  
from landing_page import display_landing_page
from pages.login import LoginPage
import os

# Set the page title
st.set_page_config(page_title="Graphly", page_icon="🐍")

# Initialize database and tables
create_tables()

def hide_sidebar_permanently():
    """ Function to hide the Streamlit sidebar permanently """
    hide_sidebar_style = """
        <style>
            [data-testid="stSidebar"] {
                display: none;
            }
            [data-testid="stSidebarNav"] {
                display: none;
            }
        </style>
    """
    st.markdown(hide_sidebar_style, unsafe_allow_html=True)

def main():
    # Initialize session states for login, signup, and access page
    if "logged_in" not in st.session_state:
        st.session_state.logged_in = False
    if "show_signup" not in st.session_state:
        st.session_state.show_signup = False
    if "access_page" not in st.session_state:
        st.session_state.access_page = None

    hide_sidebar_permanently()

    # Display landing page first
    display_landing_page()

    # if not st.session_state.logged_in:
    #     if st.session_state.show_signup:
    #         st.switch_page("pages/signup.py")  
    #     else:
    #         login_page = LoginPage()  # Create an instance of LoginPage
    #         login_page.display()  # Call the display method of LoginPage

    # else:
    #     if st.session_state.access_page:
    #         st.write(f"You are logged in and will be redirected to {st.session_state.access_page}.")
    #         # Here you would handle the actual redirection to the intended page
    #     else:
    #         st.write("You are logged in.")

if __name__ == "__main__":
    main()
