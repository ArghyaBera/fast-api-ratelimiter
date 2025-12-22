from fastapi import APIRouter

from app.routes import test, health

router = APIRouter(prefix="/v1")

# Register all route modules here
router.include_router(test.router)
router.include_router(health.router)
