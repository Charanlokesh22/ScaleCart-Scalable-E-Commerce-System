import time
from fastapi import HTTPException

RATE_LIMIT = 3
WINDOW_SECONDS = 10
rate_limit_store = {}

def rate_limiter(user_id: str):
    current_time = time.time()
    requests = rate_limit_store.get(user_id, [])

    requests = [t for t in requests if current_time - t < WINDOW_SECONDS]

    if len(requests) >= RATE_LIMIT:
        raise HTTPException(status_code=429, detail="Too many requests")

    requests.append(current_time)
    rate_limit_store[user_id] = requests
