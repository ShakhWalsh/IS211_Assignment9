# apple_stock.py
# URL: https://finance.yahoo.com/quote/AAPL/history?p=AAPL

import requests
from bs4 import BeautifulSoup

# Define URL to scrape
url = "https://finance.yahoo.com/quote/AAPL/history?p=AAPL"

# Get the HTML content
response = requests.get(url)
soup = BeautifulSoup(response.content, "html.parser")

# Locate the historical prices table
table = soup.find("table", {"class": "W(100%) M(0)"})

# Extract data from the table
if table:
    rows = table.find_all("tr")[1:]  # Skip header row

    # Print header
    print(f"{'Date':<15} {'Close Price':<10}")
    print("-" * 30)

    # Loop through rows and extract data
    for row in rows:
        cols = row.find_all("td")
        if len(cols) > 5:  # Skip rows without valid data
            date = cols[0].text.strip()
            close_price = cols[4].text.strip()
            print(f"{date:<15} {close_price:<10}")
else:
    print("Table not found!")
