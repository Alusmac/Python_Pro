from datetime import datetime, timedelta


def filter_by_days(news_list, days: int) -> list:
    """Filter news for the last N days
    """
    filtered = []
    cutoff_date = datetime.now() - timedelta(days=days)

    for news in news_list:
        try:
            news_date = datetime.strptime(news["date"], "%Y-%m-%d")
            if news_date >= cutoff_date:
                filtered.append(news)
        except:
            continue

    return filtered
