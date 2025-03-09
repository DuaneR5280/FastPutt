from fastapi import FastAPI, Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from sqlmodel import Session, SQLModel, create_engine
from typing import List, Optional
import os

# Database connection
DATABASE_URL = os.environ.get("DATABASE_URL", "postgresql://postgres:postgres@db:5432/discgolf")

# Create SQLModel engine
engine = create_engine(DATABASE_URL, echo=True)

# Create tables on startup
def create_db_and_tables():
    SQLModel.metadata.create_all(engine)

# Dependency for database sessions
def get_session():
    with Session(engine) as session:
        yield session

# Initialize FastAPI app
app = FastAPI(
    title="FastPutt API",
    description="Disc Golf API using FastAPI and SQLModel",
    version="0.1.0"
)

# Setup CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:8080"],  # Vue app default port
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Event handler for startup
@app.on_event("startup")
def on_startup():
    create_db_and_tables()

# Root endpoint for health check
@app.get("/")
def read_root():
    return {"status": "ok", "message": "FastPutt API is running"}

# For direct execution
if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)

