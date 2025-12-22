from fastapi.responses import JSONResponse
from fastapi import Request
from starlette.middleware.base import BaseHTTPMiddleware
from app.services.limiter_service import RateLimiterService
from app.repository.logs_repo import RateLimitRepository

rate_limiter = RateLimiterService()
rate_limit_repo = RateLimitRepository()

class RateLimiterMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):

        # Skip health check
        if request.url.path == "/health":
            return await call_next(request)

        endpoint = request.url.path

        allowed, remaining = rate_limiter.is_allowed(endpoint=endpoint,limit=3,window=60)

        if not allowed:
            rate_limit_repo.log(
                endpoint=endpoint,
                allowed=False,
                remaining=0,
                status_code=429
            )
            return JSONResponse(
                content={"message": "Rate limit exceeded. Please try again later."},
                status_code=429
            )

        response = await call_next(request)
        rate_limit_repo.log(
            endpoint=endpoint,
            allowed=True,
            remaining=remaining,
            status_code=response.status_code
        )
        response.headers["X-RateLimit-Remaining"] = str(remaining)
        print(response.headers)

        return response
