import React, {useState, useEffect} from 'react'
import { getGames } from '../services/api.js'
import { GameCard } from './GameCard.jsx'

function GameCardList() {
    const [games, setGames] = useState([]);
    const [loading, setLoading] = useState(true);

    useEffect(() => {
        getGames()
        .then((data) => {
            console.log("Fetched games: ", data);
            setGames(data);
            setLoading(false);
        })
        .catch((error) => {
            console.error("Failed to fetch games:", error);
            setLoading(false);
        });
    }, []);

    if (loading) {
        return <p>Loading games...</p>
    }

    return (
        <div className="games-list">
            {games.map((game) => (
                <GameCard key={game.game_id} game={game} />
            ))}
        </div>
    );
}

export default GameCardList