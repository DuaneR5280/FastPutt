from pydantic import BaseModel, Field
from typing import Optional, List
from datetime import datetime
from uuid import UUID

class StationResult(BaseModel):
    distance: int
    makes: int
    attempts: int

class RoundResult(BaseModel):
    round_id: int = Field(alias="roundId")
    round_start: datetime = Field(alias="roundStart")
    round_end: datetime = Field(alias="roundEnd")
    round_duration: float = Field(alias="roundDuration")
    round_total_makes: int = Field(alias="roundTotalMakes")
    round_total_attempts: int = Field(alias="roundTotalAttempts")
    stations: List[StationResult]

    class Config:
        allow_population_by_field_name = True
        populate_by_name = True

class GameBase(BaseModel):
    game_start: datetime = Field(alias="gameStart")
    game_end: Optional[datetime] = Field(default=None, alias="gameEnd")
    game_duration: float = Field(alias="gameDuration")
    game_rules: str = Field(alias="gameRules")
    conditions: str
    notes: str
    rounds: List[RoundResult]
    total_makes: int = Field(alias="totalMakes")
    total_attempts: int = Field(alias="totalAttempts")

    class Config:
        allow_population_by_field_name = True
        populate_by_name = True

class GameCreate(GameBase):
    pass

class GameRead(GameBase):
    id: int
    uuid: UUID

    class Config:
        allow_population_by_field_name = True
        populate_by_name = True
