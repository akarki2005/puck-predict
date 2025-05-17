import requests
from datetime import datetime, timedelta
from typing import List, Dict

def get_upcoming_games(days_ahead: int = 1) -> List[Dict]:
    """
    Fetches the list of upcoming NHL games from the official NHL API.

    Returns:
        A list of dictionaries, each representing a game with keys:
        - 'home_team': 3-letter abbreviation of the home team
        - 'away_team': 3-letter abbreviation of the away team
        - 'game_id': unique game ID
        - 'date': game start time in UTC (ISO format)
        - 'home_win_prob': placeholder win probability for the home team
        - 'away_win_prob': placeholder win probability for the away team
    """
    try:

        headers = {
            "User-Agent": "Mozilla/5.0",               # Required
            "Accept": "application/json",              # Safe default
            "Connection": "keep-alive",                # Helps in some TLS cases
        }

        url = "https://api-web.nhle.com/v1/score/now"
        response = requests.get(url, headers=headers, timeout=5)
        response.raise_for_status()
        data = response.json()

        games = data.get("games", [])
        upcoming_games = []

        now = datetime.utcnow()
        cutoff = now + timedelta(days=days_ahead)

        for game in games:
            start_time_str = game.get("startTimeUTC")
            start_time = datetime.strptime(start_time_str, "%Y-%m-%dT%H:%M:%SZ")

            if now <= start_time <= cutoff:
                upcoming_games.append({
                    "home_team": game["homeTeam"]["abbrev"],
                    "away_team": game["awayTeam"]["abbrev"],
                    "game_id": game["id"],
                    "date": start_time_str,
                    "home_win_prob": 0.5,  # Placeholder
                    "away_win_prob": 0.5   # Placeholder
                })

        return upcoming_games

    except requests.RequestException as e:
        print(f"Error fetching games: {e}")
        return []