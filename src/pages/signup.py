import streamlit as st
import sqlite3
from db import get_db_connection  # Import database functions
from interface import hide_sidebar_permanently

def signup_page():
    """ Display the signup page """
    st.title("Sign Up")

    hide_sidebar_permanently() 

    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Sign Up"):
        if register_user(username, password):
            st.success("User registered successfully!")
            # st.session_state.logged_in = True
            st.switch_page("pages/login.py")  # Redirect to the main page
        else:
            st.error("Username already exists or failed to register.")

def register_user(username, password):
    conn = get_db_connection()
    cursor = conn.cursor()
    try:
        cursor.execute('INSERT INTO users (username, password) VALUES (?, ?)', (username, password))
        conn.commit()
        return True
    except sqlite3.IntegrityError:
        return False
    finally:
        conn.close()

if __name__ == "__main__":
    signup_page()
