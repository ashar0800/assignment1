import pandas as pd
import kagglehub
import os

def fetch_kaggle_data():
    """Fetch cryptocurrency news data from Kaggle."""
    path = kagglehub.dataset_download("oliviervha/crypto-news")
    csv_file = os.path.join(path, "cryptonews.csv")
    data = pd.read_csv(csv_file)
    return data

def save_to_csv(data, filename):
    """Save data to a CSV file."""
    data.to_csv(filename, index=False)
    print(f"✅ Data saved to {filename}")

def clean_kaggle_data(data):
    """Clean Kaggle cryptocurrency news data by removing duplicates and handling missing values."""
    data.drop_duplicates(inplace=True)
    data.fillna("No Data Available", inplace=True)
    return data

def summarize_data(data, source):
    """Summarize dataset by displaying basic information."""
    print(f"\n{source} Data Summary:")
    print(data.info())
    print(data.head())

def main():
    """Main function to execute the workflow."""
    kaggle_data = fetch_kaggle_data()
    kaggle_data = clean_kaggle_data(kaggle_data)
    save_to_csv(kaggle_data, "kaggle_crypto_news.csv")
    summarize_data(kaggle_data, "Kaggle Crypto News")

if __name__ == "__main__":
    main()
