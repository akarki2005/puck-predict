from fastapi import APIRouter
from services.nhl import get_upcoming_games

router = APIRouter()

@router.get("/games")
def games():
    upcoming_games = get_upcoming_games()

    # placeholder with uniform distribution, replace with actual algorithm later
    for game in upcoming_games:
        game["home_w_prob"] = 0.5
        game["away_w_prob"] = 0.5

    return upcoming_games