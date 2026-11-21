
# Import required libraries
import requests
from bs4 import BeautifulSoup
import csv
import pandas as pd
from datetime import datetime

# Step 1: Specify the news website URL
url = "https://www.bbc.com/news"

# Step 2: Set User-Agent header
headers = {
    "User-Agent": "Mozilla/5.0"
}


def format_publication_date(value):
    if not value:
        return "N/A"

    try:
        parsed = datetime.fromisoformat(value.replace("Z", "+00:00"))
        return parsed.strftime("%Y-%m-%d %H:%M")
    except ValueError:
        return value


def extract_publication_date(article, headers):
    date_tag = article.find("time")
    if date_tag:
        value = date_tag.get("datetime") or date_tag.get_text(strip=True)
        if value:
            return format_publication_date(value)

    article_link = article.find("a", href=True)
    if not article_link:
        return "N/A"

    link = article_link["href"]
    if link.startswith("/"):
        link = "https://www.bbc.com" + link

    try:
        article_response = requests.get(link, headers=headers, timeout=10)
        if article_response.status_code != 200:
            return "N/A"

        article_soup = BeautifulSoup(
            article_response.text,
            "html.parser"
        )

        date_tag = article_soup.find("time")
        if date_tag:
            value = date_tag.get("datetime") or date_tag.get_text(strip=True)
            if value:
                return format_publication_date(value)

        for attrs in (
            {"property": "article:published_time"},
            {"name": "pubdate"},
            {"name": "publish-date"},
            {"name": "date"},
        ):
            meta_tag = article_soup.find("meta", attrs=attrs)
            if meta_tag and meta_tag.get("content"):
                return format_publication_date(meta_tag["content"])
    except requests.RequestException:
        return "N/A"

    return "N/A"

# Step 3: Send HTTP request to the website
response = requests.get(url, headers=headers, timeout=15)

# Create an empty list to store news information
news_data = []

# Step 4: Check whether the website request is successful
if response.status_code == 200:

    print("Website connected successfully!")

    # Step 5: Parse HTML content using BeautifulSoup
    soup = BeautifulSoup(response.text, "html.parser")

    # Step 6: Find all article elements
    articles = soup.select("article")

    # Step 7: Extract information from each article
    for article in articles:

        # Extract news headline
        headline_tag = article.find(["h2", "h3"])

        # Extract news category
        category_tag = article.find(
            ["span", "a"],
            attrs={"data-testid": "card-metadata-tag"}
        )

        # Get headline text
        if headline_tag:
            headline = headline_tag.get_text(strip=True)
        else:
            headline = "N/A"

        # Get publication date
        publication_date = extract_publication_date(article, headers)

        # Get category information
        if category_tag:
            category = category_tag.get_text(strip=True)
        else:
            category = "N/A"

        # Store extracted information in the list
        if headline != "N/A":
            news_data.append([
                headline,
                publication_date,
                category
            ])

    # Step 8: Save extracted information into CSV file
    with open("news_headlines.csv", "w",
              newline="", encoding="utf-8") as file:

        # Create CSV writer object
        writer = csv.writer(file)

        # Write column headings
        writer.writerow([
            "Headline",
            "Publication Date",
            "Category"
        ])

        # Write extracted news records
        writer.writerows(news_data)

    print("News data saved successfully!")

    # Step 9: Create Pandas DataFrame for analysis
    df = pd.DataFrame(
        news_data,
        columns=[
            "Headline",
            "Publication Date",
            "Category"
        ]
    )

    # Step 10: Display total number of headlines
    print("\nTotal Headlines:", len(df))

    # Step 11: Analyse news category-wise
    print("\nCategory-wise News Count:")
    print(df["Category"].value_counts())

    # Step 12: Display all extracted news information
    print("\nExtracted News Headlines:")
    print(df.to_string(index=False))

# Step 13: Display error if website request fails
else:
    print("Failed to fetch website!")
    print("Status Code:", response.status_code)
