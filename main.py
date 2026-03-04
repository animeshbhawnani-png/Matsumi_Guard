import os

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes.transactions import router as transactions_router


app = FastAPI(
    title="Cardano Risk & Compliance Engine",
    version="0.1.0",
    description="Risk and compliance scoring engine for Cardano transactions using Blockfrost.",
)

# Enable CORS for frontend
cors_allow_origins_env = os.getenv("CORS_ALLOW_ORIGINS", "")
cors_allow_origins = [
    origin.strip()
    for origin in cors_allow_origins_env.split(",")
    if origin.strip()
]

if not cors_allow_origins:
    cors_allow_origins = ["http://localhost:3000", "http://127.0.0.1:3000"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=cors_allow_origins,
    allow_origin_regex=r"https://.*\.(vercel\.app|netlify\.app)$",
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(transactions_router, prefix="/api")


@app.get("/health")
async def health_check():
    return {"status": "ok"}


@app.get("/api/test")
async def test_endpoint():
    """Test endpoint to verify backend is working"""
    return {
        "message": "Backend is running!",
        "endpoint": "/api/analyzeTransaction",
        "status": "ok"
    }


