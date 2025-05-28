from fastapi import FastAPI, Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from sqlmodel import Session, select
from datetime import datetime
from typing import List, Optional
from schemas import GameCreate, GameRead
from models import Games
from database import create_db_and_tables, get_session
from fastapi.encoders import jsonable_encoder


# Initialize FastAPI app
app = FastAPI(
    title="FastPutt API",
    description="Disc Golf API using FastAPI and SQLModel",
    version="0.1.0",
)

# Setup CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://frontend:8085",
        "http://localhost:8085",
        "http://0.0.0.0:8085",
    ],  # Vue app default port
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


@app.get("/games", response_model=List[GameRead])
async def get_games(session: Session = Depends(get_session)):
    games = session.exec(select(Games)).all()
    return games


@app.post("/games/", response_model=GameRead)
def create_game_result(
    game_result: GameCreate, session: Session = Depends(get_session)
):
    game_dict = game_result.dict()  # Use snake_case keys for the model
    game_dict["rounds"] = jsonable_encoder(game_result.rounds)
    db_game = Games(**game_dict)
    session.add(db_game)
    session.commit()
    session.refresh(db_game)

    return db_game


@app.get("/games/{uuid}", response_model=GameRead)
async def get_game(uuid: str, session: Session = Depends(get_session)):
    db_game = session.query(Games).filter(Games.uuid == uuid).first()

    if db_game is None:
        raise HTTPException(status_code=404, detail="Game not found")

    return db_game


# For direct execution
if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
