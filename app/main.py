from fastapi import FastAPI
from app.routes.urls import router as api_router
from app.middleware.rate_limiter import RateLimiterMiddleware

app = FastAPI(title="API Rate Limiting Service")
app.add_middleware(RateLimiterMiddleware)
app.include_router(api_router)
