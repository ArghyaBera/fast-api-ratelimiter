from fastapi import APIRouter

router = APIRouter()

@router.get("/test")
def test_api():
    """
    Demo endpoint to test rate limiting.
    """
    return {
        "message": "Request allowed",
        "status": "success"
    }
