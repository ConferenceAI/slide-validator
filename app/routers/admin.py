from fastapi import APIRouter, Depends, HTTPException
from app.config.settings import settings

router = APIRouter(
    prefix="/admin",
    tags=["admin"],
    responses={404: {
        "description": "Not found"
    }},
)


def get_admin_auth(api_key: str):
    if api_key != settings.api_key:
        raise HTTPException(status_code=401, detail="Invalid API Key")
    return True


@router.get("/")
async def admin_root(authorized: bool = Depends(get_admin_auth)):
    return {"message": "Welcome to the admin panel"}


@router.get("/stats")
async def get_stats(authorized: bool = Depends(get_admin_auth)):
    # Implement stats retrieval logic here
    return {"total_slides": 100, "validated_slides": 75}


@router.post("/configure")
async def configure_checks(authorized: bool = Depends(get_admin_auth)):
    # Implement configuration update logic here
    return {"message": "Configuration updated successfully"}
