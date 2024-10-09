from fastapi import FastAPI

from app.routers import slides, admin
from app.config.settings import settings

app = FastAPI(title=settings.app_name)

# Include routers
app.include_router(slides.router)
app.include_router(admin.router)


@app.get("/")
async def root():
    return {"message": f"Welcome to the {settings.app_name} API"}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
