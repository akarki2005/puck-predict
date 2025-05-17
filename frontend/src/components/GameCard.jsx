import React from 'react'

export function GameCard({game}) {
    return (
    <div className="game-card">
      <h3>{game.away_team} @ {game.home_team}</h3>
      <p>
        {Math.round(game.away_win_prob * 100)}% — {Math.round(game.home_win_prob * 100)}%
      </p>
      <p>{new Date(game.date).toLocaleString()}</p>
    </div>
    );
}