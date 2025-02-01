import streamlit as st
from scrapegraph import ScrapeAI, multi_scrape
import time
import logging

class SmartScraperMultiGraph:
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
        
        st.title('Smart Scraper Multi Graph')
        st.subheader('Multi-page scraper that extracts information from multiple pages given a single prompt and a list of sources.')
        
        self.prompt = st.text_input('Enter the prompt')

        self.urls = [st.text_input('Enter the URL')]
        num_urls = st.number_input("How many URLs do you want to scrape?", min_value=1, value=1, step=1)
        self.urls = [st.text_input(f'Enter URL {i+1}') for i in range(num_urls)]

        if st.button('Process'):
            with st.spinner('Processing...'):
                response = self._process_data(self.prompt, self.urls)

            st.json(response)


    def _process_data(self, prompt, urls):
        
        self.logger.info(f"Processing data for prompt: {self.prompt} and URLs: {self.urls}")
        response = multi_scrape(self.prompt, self.urls)

        self.logger.info("Data processing completed")
        return response

if __name__ == "__main__":
    scraper = SmartScraperMultiGraph()
    scraper.run()
