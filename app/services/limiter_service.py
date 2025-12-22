import time
from redis import Redis
from app.connections.redis_conn import get_redis_client


class RateLimiterService:
    def __init__(self):
        self.redis: Redis = get_redis_client()

        # load lua script once
        with open("app/services/ratelimiter.lua", "r") as f:
            self.lua_script = f.read()

    def is_allowed(self,endpoint: str,limit: int = 3,window: int = 60):
        """
        Sliding window rate limiter
        Returns: (allowed: bool, remaining: int)
        """

        # redis key (endpoint centric)
        redis_key = f"rate:{endpoint}"
        now = int(time.time())

        # execute lua atomically
        result = self.redis.eval(self.lua_script,1,redis_key,now,window,limit)

        allowed = result[0] == 1
        remaining = result[1]

        return allowed, remaining
