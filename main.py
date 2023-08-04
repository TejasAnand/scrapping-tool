#using serapi to scrape home depot and walmart
from dotenv import load_dotenv
import time
import Levenshtein #to check similarity of query entered by user
import os
import pandas as pd

load_dotenv()

SERPAPI_API_KEY = os.getenv('SERPAPI_API_KEY')

from serpapi import GoogleSearch

def walmart_search_results(query: str) -> list:
    params = {
        'api_key': os.getenv('SERPAPI_API_KEY'), 
        'engine': 'walmart',                      
        'query': query,                          
    }

    search = GoogleSearch(params)       

    #converting data in json from api to a dictionary           
    results = search.get_dict()                    
    
    return results.get('organic_results', [])

def get_ebay_results(query: str) -> list:
    params = {
        'api_key': os.getenv('SERPAPI_API_KEY'),    # https://serpapi.com/manage-api-key
        'engine': 'ebay',                           # search engine
        '_nkw': query,                              # search query
        'ebay_domain': 'ebay.com',                  # ebay domain
    }

    search = GoogleSearch(params)                     # data extraction on the SerpApi backend
    results = search.get_dict()                     # JSON -> Python dict
    
    return results.get('organic_results', [])


