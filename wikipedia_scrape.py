# wikipedia_scrape.py
# URL: https://en.wikipedia.org/wiki/List_of_Super_Bowl_champions

import requests
from bs4 import BeautifulSoup
import pandas as pd

# Define URL to scrape
url = "https://en.wikipedia.org/wiki/List_of_Super_Bowl_champions"

# Get the HTML content
response = requests.get(url)
soup = BeautifulSoup(response.content, "html.parser")

# Locate the first table on the page
table = soup.find("table", {"class": "wikitable"})

# Use pandas to read the HTML table into a DataFrame
df = pd.read_html(str(table))[0]

# Print the first 5 rows
print(df.head())
