from datetime import datetime
from app.connections.mongo_conn import get_db

class RateLimitRepository:
    def __init__(self):
        self.collection = get_db()["rate-limit-logs"]

    def log(self, endpoint: str, allowed: bool, remaining: int, status_code: int):
        self.collection.insert_one({
            "endpoint": endpoint,
            "allowed": allowed,
            "remaining": remaining,
            "status_code": status_code,
            "timestamp": datetime.utcnow()
        })
