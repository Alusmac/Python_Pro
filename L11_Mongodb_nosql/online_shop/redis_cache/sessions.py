import redis
from datetime import datetime, timezone
import uuid

r = redis.Redis(host="localhost", port=6379, decode_responses=True)
SESSION_TTL = 1800


def create_session(user_id: str) -> str:
    """create new session
    """
    session_token = str(uuid.uuid4())
    key = f"session:{session_token}"

    r.hset(key, mapping={
        "user_id": user_id,
        "login_time": datetime.now(timezone.utc).isoformat(),
        "last_activity": datetime.now(timezone.utc).isoformat()
    })
    r.expire(key, SESSION_TTL)
    return session_token


def get_session(session_token: str) -> dict | None:
    """get session
    """
    key = f"session:{session_token}"
    if not r.exists(key):
        return None
    return r.hgetall(key)


def update_last_activity(session_token: str) -> None:
    """update last activity user
    """
    key = f"session:{session_token}"
    if r.exists(key):
        r.hset(key, "last_activity", datetime.now(timezone.utc).isoformat())
        r.expire(key, SESSION_TTL)


def delete_session(session_token: str) -> None:
    """delete session
    """
    r.delete(f"session:{session_token}")
