import pandas as pd
import yfinance as yf

def fetch_yahoo_finance_data():
    """Fetch Bitcoin stock data from Yahoo Finance."""
    stock = yf.Ticker("BTC-USD")
    stock_info = {
        "Name": stock.info.get('longName', 'N/A'),
        "Market Cap": stock.info.get('marketCap', 'N/A'),
        "Current Price": stock.history(period='1d')['Close'].iloc[-1]  # Latest closing price
    }
    historical_data = stock.history(period="6mo")
    return stock_info, historical_data

def save_to_csv(data, filename):
    """Save data to a CSV file."""
    data.to_csv(filename, index=False)
    print(f"✅ Data saved to {filename}")

def summarize_data(data, source):
    """Summarize dataset by displaying basic information."""
    print(f"\n{source} Data Summary:")
    print(data.info())
    print(data.head())

def main():
    """Main function to execute the workflow."""
    stock_info, historical_data = fetch_yahoo_finance_data()
    save_to_csv(historical_data, "yahoo_finance_data.csv")
    summarize_data(historical_data, "Yahoo Finance Historical Data")

if __name__ == "__main__":
    main()
