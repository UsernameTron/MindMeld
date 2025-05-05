from fastapi import FastAPI
from app.api.routes import analyze

app = FastAPI()

@app.get("/health")
async def health_check():
    return {"status": "healthy"}

app.include_router(analyze.router)
