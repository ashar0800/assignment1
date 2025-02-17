import praw
import csv
from datetime import datetime, timezone
import pandas as pd
def fetch_reddit_data():
    """Fetch posts from Reddit related to cryptocurrency."""
    reddit = praw.Reddit(
        client_id="TlXppNw85D_UYkkFoZ1plQ",
        client_secret="r_eIOkd79ZgympVtKr_HkC85xP44OA",
        user_agent="crypto_api"
    )
    subreddit = reddit.subreddit("all")
    keywords = ["Bitcoin", "Blockchain", "Cryptocurrency"]
    posts = [
        [
            post.title,
            post.selftext,
            post.author.name if post.author else "[Deleted]",
            datetime.fromtimestamp(post.created_utc, timezone.utc).strftime('%Y-%m-%d %H:%M:%S'),
            post.score,
            post.subreddit.display_name
        ]
        for post in subreddit.search(keywords, limit=200)
    ]
    return posts

def save_to_csv(data, filename, headers):
    """Save data to a CSV file."""
    with open(filename, "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(headers)
        writer.writerows(data)
    print(f"✅ Data saved to {filename}")

def clean_reddit_data(filename):
    """Clean Reddit data by removing duplicates and handling missing text."""
    df = pd.read_csv(filename)
    df.drop_duplicates(subset=["Title", "Post Text"], inplace=True)
    df["Post Text"].fillna("No Text Available", inplace=True)
    df["Post Text"] = df["Post Text"].astype(str).str.lower()
    return df

def summarize_reddit_data(df):
    """Summarize Reddit data by counting key terms and showing top posts."""
    bull_count = df["Post Text"].str.count(r"\\bbull\\b").sum()
    bear_count = df["Post Text"].str.count(r"\\bbear\\b").sum()
    invest_count = df["Post Text"].str.count(r"\\binvest\\b").sum()
    print(f"Count of 'bull': {bull_count}")
    print(f"Count of 'bear': {bear_count}")
    print(f"Count of 'invest': {invest_count}")
    print("\nTop 5 Posts by Upvotes:")
    print(df.sort_values(by="Upvotes", ascending=False).head())

def main():
    """Main function to fetch, clean, save, and summarize data."""
    # Fetch and save Reddit data
    reddit_posts = fetch_reddit_data()
    save_to_csv(reddit_posts, "reddit_crypto_posts.csv", ["Title", "Post Text", "Author", "Date", "Upvotes", "Subreddit"])
    reddit_df = clean_reddit_data("reddit_crypto_posts.csv")
    summarize_reddit_data(reddit_df)

if __name__=="__main__":
    main()
