import streamlit as st
from scrapegraph import ScrapeAI, script_creator_multi
import time
import logging

class ScriptCreatorMultiGraph:
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
        
        st.title('ScriptCreatorMultiGraph')
        st.subheader('Multi-page scraper that generates a Python script for extracting information from multiple pages and sources.')

        self.prompt = st.text_input('Enter the prompt')

       
        num_urls = st.number_input("How many URLs do you want to scrape?", min_value=1, value=1, step=1)
        self.urls = [st.text_input(f'Enter URL {i+1}') for i in range(num_urls)]

        if st.button('Process'):
            with st.spinner('Processing...'):
                response = self._process_data(self.prompt, self.urls)

            st.code(response, language='python')

    def _process_data(self, prompt, urls):
    
        self.logger.info(f"Processing data for prompt: {self.prompt} and URLs: {self.urls}")
        response = script_creator_multi(self.prompt, self.urls)

        self.logger.info("Data processing completed")
        return response

if __name__ == "__main__":
    scraper = ScriptCreatorMultiGraph()
    scraper.run()
