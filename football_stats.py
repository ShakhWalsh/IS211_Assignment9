# football_stats.py
# URL: https://www.cbssports.com/nfl/stats/leaders/

import requests
from bs4 import BeautifulSoup

# Define URL to scrape
url = "https://www.cbssports.com/nfl/stats/leaders/"

# Get the HTML content
response = requests.get(url)
soup = BeautifulSoup(response.content, "html.parser")

# Locate the touchdowns table
table = soup.find("table", {"class": "TableBase-table"})

# Extract data from the table
if table:
    rows = table.find_all("tr")[1:21]  # Get top 20 rows (skip header)

    # Print header
    print(f"{'Player':<25} {'Position':<10} {'Team':<10} {'TDs':<5}")
    print("-" * 50)

    # Loop through rows and extract player data
    for row in rows:
        cols = row.find_all("td")
        player_name = cols[0].text.strip()
        position = cols[1].text.strip()
        team = cols[2].text.strip()
        touchdowns = cols[6].text.strip()

        # Print player details
        print(f"{player_name:<25} {position:<10} {team:<10} {touchdowns:<5}")
else:
    print("Table not found!")
