import requests
from bs4 import BeautifulSoup
from datetime import datetime
from filters import filter_by_days
from csv_saver import save_to_csv
import pandas as pd

BASE_URL = "https://www.cbsnews.com"
WORLD_URL = "https://www.cbsnews.com/world/"
CSV_FILENAME = "cbs_world_news.csv"
DAYS_FILTER = 7


def get_page(url: str) -> BeautifulSoup:
    """Loading  World HTML page
    """
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        return BeautifulSoup(response.text, "html.parser")
    except requests.exceptions.RequestException as e:
        print(f"[ERROR] Failed to fetch page: {e}")
        return None


def parse_news(soup) -> list:
    """Parsing news from the page
    """
    news_list = []

    if not soup:
        return news_list

    articles = soup.find_all("article")

    for article in articles:
        try:
            title_tag = article.find("h4") or article.find("h3")
            if not title_tag:
                continue

            title = title_tag.get_text(strip=True)

            link_tag = article.find("a", href=True)
            link = link_tag["href"] if link_tag else None

            if link and not link.startswith("http"):
                link = BASE_URL + link

            time_tag = article.find("time")
            if time_tag and time_tag.has_attr("datetime"):
                date = time_tag["datetime"][:10]
            else:
                date = datetime.today().strftime("%Y-%m-%d")

            summary_tag = article.find("p")
            summary = summary_tag.get_text(strip=True) if summary_tag else ""

            news_list.append({
                "title": title,
                "link": link,
                "date": date,
                "summary": summary
            })

        except Exception as e:
            print(f"[ERROR] Parsing failed: {e}")

    return news_list


def generate_stats(data: list) -> None:
    """News statistics by day
    """
    if not data:
        print("No data for statistics")
        return

    df = pd.DataFrame(data)
    df["date"] = pd.to_datetime(df["date"])
    stats = df.groupby(df["date"].dt.date).size()

    print("\n📰 News count by date:")
    print(stats)


def main() -> None:
    soup = get_page(WORLD_URL)
    news = parse_news(soup)

    print(f"Total scraped: {len(news)}")

    filtered_news = filter_by_days(news, DAYS_FILTER)

    save_to_csv(filtered_news, CSV_FILENAME)
    generate_stats(filtered_news)


if __name__ == "__main__":
    main()
