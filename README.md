# MyAnimeList-Score-Scraper
A web scraper specified for scraping score data from MyAnimeList using Playwright for Python library and SQLalchemy

# INTRO
1. **THE WHAT**

This is a web scraper that created specify for scraping MyAnimeList scoring data. It using a combination of Playwrigth for Python, BeautifulSoup, and SQLalchemy to extract HTML, transform, and store the data to a database.

2. **THE WHY**

I like anime. I like data. I'm curious of what is the highest score anime in MyAnimeList. I'm curious to know many things about anime data. And MyAnimeList have quite enough data to explore. So, why not?


3. **THE HOW**

I'm using "Extract, Transform, Load" process when I scraping and storing the data I got from MyAnimeList.


# PARTS
I choose to separate this project into three files:
1. **playwright_scraper.py**

  This is where I made the main webscraper functionality. It consist of two functions:
  
      a. anime_season()
      
          This is a function I made to classify anime into their respective airing season.
  
      b. playwright_scraper()
      
          The main function for extracting and transforming the data of each pages. It accepting anime genre URL from myanimelist as its input. 
          It will then open each pages of genre feed into it, checking if the page exist, and take the page's HTML ready to be rendered by BeautifulSoup. 
          BeautifulSoup then parsing (transform) the HTML file into informations like anime name, average score, and their genre(s).
  
2. **modeler.py**

  Modeler is just a file I use to create database. I'm using SQLite as my database of choice and SQLAlchemy as a tool to create it.

3. **etl_process.py**

This file is used to automate the process of extracting, transforming, and loading data from MyAnimeList website into the database. It consists of a variable to getting date (I'm using this to create unique table name in SQLite), a list of URL of the targeted genres, and a for loop that will feed each URL in the list into playwright_scraper() function that will produce a dictionary of anime genre. The dictionary then used as an input to  populate the database by using modeler() function.
  
