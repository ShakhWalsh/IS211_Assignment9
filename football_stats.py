# football_stats.py
import requests
from bs4 import BeautifulSoup

# Define the URL to scrape
url = "https://www.cbssports.com/nfl/stats/player/scoring/nfl/regular/qualifiers/"

# Add headers to simulate a browser request
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36"
}

# Get the HTML content of the page
response = requests.get(url, headers=headers)

# Check if the request was successful
if response.status_code != 200:
    print(f"Failed to load page, status code: {response.status_code}")
    exit()

# Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(response.content, "html.parser")

# Locate the correct table containing player data
table = soup.find("table", {"class": "TableBase-table"})

# Verify if the table is found
if not table:
    print("Table not found! Check the class or URL.")
    exit()

# Extract all rows from the table (skip the header row)
rows = table.find("tbody").find_all("tr")

# Print header for clarity
print(f"{'Player':<25} {'Position':<10} {'Team':<10} {'TDs':<5}")
print("-" * 55)

# Loop through the first 20 rows and extract player data
for row in rows[:20]:  # Get the top 20 players
    cols = row.find_all("td")

    # Skip rows that do not have enough columns
    if len(cols) >= 13:
        # Extract player name from the correct span tag
        player_name = cols[0].find("a").text.strip()

        # Extract position and team from nested span elements
        position = cols[0].find("span", {"class": "CellPlayerName-position"}).text.strip()
        team = cols[0].find("span", {"class": "CellPlayerName-team"}).text.strip()

        # Touchdowns are in the 13th column (cols[12])
        touchdowns = cols[12].text.strip()

        # Print only valid rows
        if player_name and position and team and touchdowns != "—":
            print(f"{player_name:<25} {position:<10} {team:<10} {touchdowns:<5}")
