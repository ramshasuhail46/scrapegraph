import streamlit as st
from scrapegraph import ScrapeAI, script_creator
import time
import logging

class ScriptCreatorGraph:
    def __init__(self):
        self.logger = self._setup_logger()
        self.prompt = ""
        self.urls = []
        self.scraper = ScrapeAI()

    def _setup_logger(self):
        logger = logging.getLogger(__name__)
        logger.setLevel(logging.INFO)
        handler = logging.StreamHandler()
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        handler.setFormatter(formatter)
        logger.addHandler(handler)
        return logger

    def check_login(self):
        """ Check if the user is logged in, and redirect to login page if not """
        if not st.session_state.get("logged_in", False):
            st.error("You are not logged in! Redirecting to the login page...")
            time.sleep(1)  
            st.switch_page("interface.py")

    def run(self):

        self.check_login()
        
        st.title("Script Creator Graph")
        st.subheader('Single-page scraper that extracts information from a website and generates a Python script.')

        self.prompt = st.text_input('Enter the prompt')

        self.urls = [st.text_input('Enter the URL')]

        if st.button('Process'):
            with st.spinner('Processing...'):
                response = self._process_data(self.prompt, self.urls)

            st.code(response, language='python')

    def _process_data(self, prompt, url):
        self.logger.info(f"Processing data for prompt: {self.prompt} and URL: {self.urls[0]}")
        response = script_creator(self.prompt, self.urls[0])
        self.logger.info("Data processing completed")
        return response

if __name__ == "__main__":
    scraper = ScriptCreatorGraph()
    scraper.run()
