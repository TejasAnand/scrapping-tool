#using serapi to scrape home depot and walmart
from dotenv import load_dotenv
import time
import Levenshtein #to check similarity of query entered by user
import os
import pandas as pd

load_dotenv()

SERPAPI_API_KEY = os.getenv('SERPAPI_API_KEY')

from serpapi import GoogleSearch
