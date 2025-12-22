import redis

# Create Redis client
redis_client = redis.Redis(
    host="localhost",
    port=6379,
    db=0,
    decode_responses=True 
)

def get_redis_client():
    """
    Returns Redis client instance
    """
    return redis_client
