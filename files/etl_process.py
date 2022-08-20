from playwright.sync_api import sync_playwright
from bs4 import BeautifulSoup as bs
import re
from datetime import datetime

from playwright_scraper import *
from modeler import *

# Preparation

date = datetime.now().strftime('%d%m%y')

# EXTRACT AND TRANSFORM

url_list = [   
    'https://myanimelist.net/anime/genre/1/',  # Action
    'https://myanimelist.net/anime/genre/2/',  # Adventure
    'https://myanimelist.net/anime/genre/5/',  # Avant Garde
    'https://myanimelist.net/anime/genre/4/',  # Comedy
    'https://myanimelist.net/anime/genre/8/',  # Drama
    'https://myanimelist.net/anime/genre/10/', # Fantasy
    'https://myanimelist.net/anime/genre/47/', # Gourmet
    'https://myanimelist.net/anime/genre/14/', # Horror
    'https://myanimelist.net/anime/genre/7/',  # Mystery
    'https://myanimelist.net/anime/genre/22/', # Romance
    'https://myanimelist.net/anime/genre/24/', # Sci-fi
    'https://myanimelist.net/anime/genre/36/', # Slice-of-life
    'https://myanimelist.net/anime/genre/30/', # Sport
    'https://myanimelist.net/anime/genre/37/', # Supernatural
    'https://myanimelist.net/anime/genre/41/'  # Suspense
]

if __name__ == '__main__':
    for url in url_list:
        for data in playwright_scraper(url, 100):
            modeler(date, data)



# modeler(date, extracted_data)