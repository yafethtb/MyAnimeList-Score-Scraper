from playwright.sync_api import sync_playwright
from bs4 import BeautifulSoup as bs
import re
from time import sleep


def anime_season(month):
    '''Labeling each month with their respected TV season'''
    month_num = int(month)
    if month_num in range(1, 4):
        return 'Winter'
    elif month_num in range(4, 7):
        return 'Spring'
    elif month_num in range(7, 10):
        return 'Summer'
    elif month_num in range(10, 13):
        return 'Fall'
    else:
        return 'Unspecified' 

def playwright_scraper(url, last):
    # Create container
    container = []

    # Execute synchronous playwright
    with sync_playwright() as p:
        # Initialize 
        browser = p.chromium.launch()
        page = browser.new_page()
        page.goto(url)
        data_name = page.inner_text('.h1').split()[0]

        # Iterating
        for page_num in range(1, last + 1):
            sleep(1.5)
            new_url = url + f'?page={page_num}'
            page.goto(new_url)
            flag = page.query_selector('.error404')

            if not flag:                      
                anime_list = page.query_selector_all('.js-anime-category-producer')

                # Parsing               
                for html_item in anime_list:
                    html = html_item.inner_html()
                    anime = bs(html, 'html.parser')

                    # Scraping data
                    container.append(
                        {
                            'Title': anime.find('span', class_='js-title').text,
                            'Voters': int(anime.find('span', class_='js-members').text),
                            'Avg Score': float(anime.find('span', class_='js-score').text),
                            'Year': anime.find('span', class_='js-start_date').text[:4],
                            'Season': anime_season(anime.find('span', class_='js-start_date').text[4:6]),
                            'Studio': [studio.text.strip() for studio in anime.find('div', class_='properties')][1].replace('Studio', ''),
                            'Genre(s)': ', '.join([data.text.strip() for data in anime.find('div', class_= 'genres-inner js-genre-inner').select('span')]),
                            'Media': re.sub(r'[\W+\d]', '', [data.text for data in anime.find('div', class_='info').select('span')][0]),
                            'Status': [data.text for data in anime.find('div', class_='info').select('span')][1],
                            'Eps': [data.text.split()[0] for data in anime.find('div', class_='info').select('span')][2],
                            'Duration(min)': [data.text.split()[0] for data in anime.find('div', class_='info').select('span')][-1],
                        }
                    )
            else:
                # Break out 
                print(f'Page {page_num} of {data_name} genre is not existed')
                break

        # Close Browser
        browser.close()

    # Return list of dictionary
    return container