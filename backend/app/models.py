from sqlmodel import SQLModel, Field, JSON
from sqlalchemy import Column
from datetime import datetime
from uuid import UUID, uuid4
from typing import Dict, Optional, List
from schemas import StationResult, RoundResult


class Games(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    uuid: UUID = Field(default_factory=uuid4, unique=True, nullable=False)
    game_start: datetime
    game_end: Optional[datetime] = None
    game_duration: float
    game_rules: str
    conditions: str
    notes: str
    rounds: list = Field(sa_column=Column(JSON))
    total_makes: int
    total_attempts: int
