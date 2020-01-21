# goals:
# - webscraper that can search pasted user input
# - flexible and decent i guess

# functionality:
# paste url in input
# search for specific text/tags

import requests
import urllib.request
import time
from bs4 import BeautifulSoup
import pandas as pd

def scrape():
    page = requests.get(menu())
    print(page.content)

def menu():
    url = input("Paste URL here:")
    return url


if __name__ == "__main__":
    menu()