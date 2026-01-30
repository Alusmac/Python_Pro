from datetime import datetime, timezone, timedelta


def days_ago(days: int) -> datetime:
    """Return datetime N days ago in UTC
    """
    return datetime.now(timezone.utc) - timedelta(days=days)
