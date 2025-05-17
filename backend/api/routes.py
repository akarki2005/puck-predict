from fastapi import APIRouter
from services.nhl import get_upcoming_games

router = APIRouter()

@router.get("/games")
def games():
    return get_upcoming_games()