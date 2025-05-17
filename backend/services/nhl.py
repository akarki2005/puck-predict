import requests
from datetime import datetime, timedelta
from typing import List, Dict, Any

def get_upcoming_games(days_ahead: int = 7) -> List[Dict[str, Any]]:
    """
    Get a list of upcoming games for the next days_ahead days.
    By default, get the next week of games.
    """

    format = "%Y:%m:%d"
    today = datetime.now().strftime(format)
    end_date = (datetime.now() + timedelta(days=days_ahead)).strftime(format)

    url = f"https://statsapi.web.nhl.com/api/v1/schedule?startDate={today}&endDate={end_date}"
    # GET from api
    response = requests.get(url)
    # check for errors
    response.raise_for_status()
    # store response in data
    data = response.json()

    games = []
    for date in data.get("dates", []):
        for game in date.get("games", []):
            game = {
                "date": game["gameDate"],
                "home_team": game["teams"]["home"]["team"]["name"],
                "away_team": game["teams"]["away"]["team"]["name"],
                "home_team_id": game["teams"]["home"]["team"]["id"],
                "away_team_id": game["teams"]["away"]["team"]["id"],
                "game_id": game["gamePk"]
            }
            games.append(game)

    return games