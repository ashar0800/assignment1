import pandas as pd
from pytrends.request import TrendReq

def fetch_google_trends_data():
    """Fetch Google Trends data for cryptocurrency topics."""
    pytrends = TrendReq(hl='en-US', tz=0)
    keywords = ["Bitcoin", "Blockchain", "Cryptocurrency"]
    pytrends.build_payload(keywords, timeframe="today 12-m", geo="")
    data = pytrends.interest_over_time().infer_objects(copy=False)
    return data

def save_to_csv(data, filename):
    """Save data to a CSV file."""
    data.to_csv(filename, index=False)
    print(f"✅ Data saved to {filename}")

def clean_google_trends_data(data):
    """Clean Google Trends data by removing incomplete columns and resetting index."""
    if "isPartial" in data.columns:
        data.drop(columns=["isPartial"], inplace=True)
    data.reset_index(inplace=True)
    return data

def summarize_google_trends_data(data):
    """Summarize Google Trends data by displaying basic information."""
    print("\nGoogle Trends Data Summary:")
    print(data.info())
    print(data.head())

def main():
    """Main function to execute the workflow."""
    data = fetch_google_trends_data()
    data = clean_google_trends_data(data)
    save_to_csv(data, "google_trends_crypto.csv")
    summarize_google_trends_data(data)

if __name__ == "__main__":
    main()