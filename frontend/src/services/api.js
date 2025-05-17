export function getGames() {
    return fetch("/games")
    .then((result) => {
        if (!result.ok) {
            throw new Error(`Failed to fetch /games: ${result.statusText}`);
        }
        return result.json();
    })
}