# apple_stock.py
import yfinance as yf
import pandas as pd

# Define the stock ticker symbol
ticker_symbol = "AAPL"

# Get the historical stock data
apple_data = yf.download(ticker_symbol, period="1mo", interval="1d")

# Check if data is valid
if apple_data.empty or "Close" not in apple_data.columns:
    print("No data found or 'Close' column missing. Check the ticker symbol or parameters.")
    exit()

# Flatten the column names to handle MultiIndex
if isinstance(apple_data.columns, pd.MultiIndex):
    apple_data.columns = ["_".join(col).strip() for col in apple_data.columns.values]

# Reset the index to make 'Date' a column
apple_data.reset_index(inplace=True)

# Print header for clarity
print(f"{'Date':<15} {'Close Price':<10}")
print("-" * 30)

# Corrected column name for Close price
close_col_name = "Close_AAPL"  # Since the column name is flattened

# Loop through the rows and print date and close price
for _, row in apple_data.iterrows():
    date = row["Date"]
    close_price = row[close_col_name]

    # Handle Series or NaN values correctly
    if isinstance(date, pd.Timestamp) and pd.notnull(close_price):
        print(f"{date.strftime('%Y-%m-%d'):<15} {float(close_price):<10.2f}")
