from scrapegraphai.graphs import SearchGraph, SmartScraperGraph, SmartScraperMultiGraph, ScriptCreatorGraph, ScriptCreatorMultiGraph, SpeechGraph
# from google.cloud import texttospeech
from dotenv import load_dotenv
import os
import logging

class ScrapeAI:
    def __init__(self):
        load_dotenv()
        self.logger = self._setup_logger()
        self.model = os.getenv("MODEL")
        self.base_url = os.getenv("BASE_URL")
        self.model_tokens = os.getenv("MODEL_TOKENS")
        self.key = os.getenv("KEY")
        self.logger.info("ScrapeAI initialized with environment variables")

    def _setup_logger(self):
        logger = logging.getLogger(__name__)
        logger.setLevel(logging.INFO)
        handler = logging.StreamHandler()
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        handler.setFormatter(formatter)
        logger.addHandler(handler)
        return logger



    def search_graph(self, prompt):
        self.logger.info(f"Starting search and scrape operation. ")
        graph_config = {
            "llm": {
                "model": self.model,
                "temperature": 0.5,
                "format": "json",
                "model_tokens": self.model_tokens,
                "base_url": self.base_url
            },
            "scraper": {
                "max_depth": 3,
                "max_links": 30,
                "custom_settings": {
                    "ROBOTSTXT_OBEY": True,
                    "USER_AGENT": "Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)"
                }
            },
            "summarizer": {
                "chunk_size": 2000,
                "chunk_overlap": 200
            }
        }

        search_scrape_graph = SearchGraph(
            prompt=prompt,
            config=graph_config
        )

        self.logger.info("Running SearchGraph for search and scrape operation")
        result = search_scrape_graph.run()

        if isinstance(result, dict):
            result['metadata'] = {
                'scrape_depth': graph_config['scraper']['max_depth'],
                'pages_scraped': len(result.get('pages', [])),
                'search_query': prompt
            }

        self.logger.info(f"Search and scrape operation completed. Scraped {result['metadata']['pages_scraped']} pages.")
        return result

    def smart_scraper_multi(self, prompt, urls):
        self.logger.info(f"Starting multi-URL smart scraper operation for {len(urls)} URLs")
        graph_config = {
            "llm": {
                "model": self.model,
                "temperature": 0.7,
                "format": "json",
                "model_tokens": self.model_tokens,
                "base_url": self.base_url
            },
            "scraper": {
                "max_depth": 3,
                "max_links": 20,
                "custom_settings": {
                    "ROBOTSTXT_OBEY": True,
                    "USER_AGENT": "Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)"
                }
            },
            "summarizer": {
                "chunk_size": 2500,
                "chunk_overlap": 250
            }
        }

        smart_scraper_multi_graph = SmartScraperMultiGraph(
            prompt=prompt,
            source=urls,
            config=graph_config
        )

        self.logger.info("Running SmartScraperMultiGraph for multi-URL scraping and analysis")
        result = smart_scraper_multi_graph.run()

        # Post-processing for detailed results
        if isinstance(result, dict):
            result['metadata'] = {
                'source_urls': urls,
                'urls_scraped': len(urls),
                'total_pages_scraped': sum(len(url_result.get('pages', [])) for url_result in result.get('url_results', [])),
                'search_query': prompt
            }

            # Add detailed information for each URL
            for url_result in result.get('url_results', []):
                url_result['metadata'] = {
                    'source_url': url_result.get('url'),
                    'scrape_depth': graph_config['scraper']['max_depth'],
                    'pages_scraped': len(url_result.get('pages', [])),
                    'main_topics': url_result.get('main_topics', []),
                    'sentiment': url_result.get('sentiment', 'neutral')
                }

        self.logger.info(f"Multi-URL smart scraper operation completed. Scraped {result['metadata']['total_pages_scraped']} pages across {result['metadata']['urls_scraped']} URLs.")
        return result

    def scrape(self, prompt, url):
        self.logger.info(f"Starting SmartScraperGraph for e-commerce product scrape operation for URL: {url}")
        graph_config = {
            "llm": {
                "model": self.model,
                "temperature": 0.3,  # Lower temperature for more precise product information
                "format": "json",
                "model_tokens": self.model_tokens,
                "base_url": self.base_url
            },
            "scraper": {
                "max_depth": 5,  # Increased depth to navigate through product categories
                "max_links": 50,  # Increased to cover more product pages
                "allowed_domains": [url.split("//")[-1].split("/")[0]],  # Restrict to the main domain
                "custom_settings": {
                    "ROBOTSTXT_OBEY": True,
                    "USER_AGENT": "Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)"
                }
            },
            "summarizer": {
                "chunk_size": 3000,  # Increased for more comprehensive product descriptions
                "chunk_overlap": 300
            }
        }

        enhanced_prompt = f"Extract and list all products from this e-commerce website. For each product, provide: name, price, description, image URL (if available), and any other relevant details such as variants, sizes, or colors. {prompt}"

        smart_scraper_graph = SmartScraperGraph(
            prompt=enhanced_prompt,
            source=url,
            config=graph_config,
        )

        self.logger.info("Running SmartScraperGraph for e-commerce product extraction")
        result = smart_scraper_graph.run()
        
        # Post-processing for product-specific results
        if isinstance(result, dict):
            result['metadata'] = {
                'source_url': url,
                'scrape_depth': graph_config['scraper']['max_depth'],
                'products_found': len(result.get('products', [])),
                'categories_scraped': result.get('categories_scraped', [])
            }
        
        self.logger.info(f"E-commerce product scrape operation completed. Found {result['metadata']['products_found']} products.")
        return result
    
    def ScriptCreatorGraph(self, prompt, url):
        self.logger.info(f"Starting ScriptCreatorGraph  operation for URL: {url}")
        graph_config = {
            "llm": {
                "model": self.model,
                "temperature": 0.3,  # Lower temperature for more precise product information
                "format": "json",
                "model_tokens": self.model_tokens,
                "base_url": self.base_url
            },
            "scraper": {
                "max_depth": 5,  # Increased depth to navigate through product categories
                "max_links": 50,  # Increased to cover more product pages
                "allowed_domains": [url.split("//")[-1].split("/")[0]],  # Restrict to the main domain
                "custom_settings": {
                    "ROBOTSTXT_OBEY": True,
                    "USER_AGENT": "Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)"
                }
            },
            "summarizer": {
                "chunk_size": 3000,  # Increased for more comprehensive product descriptions
                "chunk_overlap": 300
            },
            "library": {"beautifulsoup4": "4.10.0",
            }
        }
        

        enhanced_prompt = f"""
            Create a Python script using BeautifulSoup4 to scrape product details from the website at {url}.
            {prompt}
        """

        scriptcreatorgraph = ScriptCreatorGraph(
            prompt=enhanced_prompt,
            source=url,
            config=graph_config,
        )

        self.logger.info("Running ScriptCreatorGraph for code")
        result = scriptcreatorgraph.run()
        
        self.logger.info(f"ScriptCreatorGraph operation completed")
        return result
    
    def ScriptCreatorMulti(self, prompt, url):
        self.logger.info(f"Starting operation for URL: {url}")
        graph_config = {
            "llm": {
                "model": self.model,
                "temperature": 0.3,  # Lower temperature for more precise product information
                "format": "json",
                "model_tokens": self.model_tokens,
                "base_url": self.base_url
            },
            "library": {"beautifulsoup4": "4.10.0"
            }
        }

        enhanced_prompt = f"""
            Create a Python script using BeautifulSoup4 to scrape details from the website at {url}.
            {prompt}
        """

        scriptcreatormultigraph = ScriptCreatorMultiGraph(
            prompt=enhanced_prompt,
            source=url,
            config=graph_config,
        )

        self.logger.info("Running ScriptCreatorMultiGraph for e-commerce product extraction")
        result = scriptcreatormultigraph.run()
        return result
    
    def speech_graph(self, prompt, url):
        self.logger.info(f"Starting speech_graph for e-commerce product scrape operation for URL: {url}")
        graph_config = {
            "llm": {
                "model": self.model,
                "temperature": 0.3,  # Lower temperature for more precise product information
                "format": "json",
                "model_tokens": self.model_tokens,
                "base_url": self.base_url
            },
            "scraper": {
                "max_depth": 5,  # Increased depth to navigate through product categories
                "max_links": 50,  # Increased to cover more product pages
                "allowed_domains": [url.split("//")[-1].split("/")[0]],  # Restrict to the main domain
                "custom_settings": {
                    "ROBOTSTXT_OBEY": True,
                    "USER_AGENT": "Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)"
                }
            },
            "summarizer": {
                "chunk_size": 3000,  # Increased for more comprehensive product descriptions
                "chunk_overlap": 300
            },
            "tts_model": {
                # "model_id": "googleapis"
                "api_key": self.key, 
                "model_tokens": self.model_tokens,  
                "voice": "en-US-Wavenet-D",  
                "format": "mp3", 
                "speed": 1.0,
                "pitch": 0  
            },   
        }

        self.logger.info(f"Starting speech_graph for e-commerce product scrape operation for URL: {url}")
        
        # Scraping and configuration logic remains the same
        # Constructing the enhanced prompt
        enhanced_prompt = f"Extract and list all products from this e-commerce website. For each product, provide: name, price, description, image URL (if available), and any other relevant details such as variants, sizes, or colors. {prompt}"

        self.logger.info("Running speech_graph for e-commerce product extraction")

        # Scraping and post-processing logic
        speechgraph = SpeechGraph(
            prompt=enhanced_prompt,
            source=url,
            config=graph_config,
        )
        result = speechgraph.run()

        # Post-processing for product-specific results
        if isinstance(result, dict):
            result['metadata'] = {
                'source_url': url,
                'scrape_depth': graph_config['scraper']['max_depth'],
                'products_found': len(result.get('products', [])),
                'categories_scraped': result.get('categories_scraped', [])
            }

        self.logger.info(f"E-commerce product scrape operation completed. Found {result['metadata']['products_found']} products.")
        return result

def scraperai(prompt, url):
    scraper = ScrapeAI()
    return scraper.scrape(prompt, url)

def speech_graph_function(prompt, url):
    scraper = ScrapeAI()
    return scraper.speech_graph(prompt, url)

def script_creator(prompt, url):
    scraper = ScrapeAI()
    return scraper.ScriptCreatorGraph(prompt, url)

def script_creator_multi(prompt, url):
    scraper = ScrapeAI()
    return scraper.ScriptCreatorMulti(prompt, url)

def multi_scrape(prompt, urls):
    scraper = ScrapeAI()
    return scraper.smart_scraper_multi(prompt, urls)

def search_graph(prompt):
    scraper = ScrapeAI()
    return scraper.search_graph(prompt)


