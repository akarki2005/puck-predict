import { useState } from 'react'
import reactLogo from './assets/react.svg'
import viteLogo from '/vite.svg'
import './App.css'
import GameCardList from './components/GameCardList'

function App() {

  console.log("App loaded");
  return (
    <div className="min-h-screen flex flex-col items-center justify-center bg-gray-100">
      <h1 className="text-4xl font-bold text-blue-600">Puck Predict</h1> 
      <GameCardList />
    </div>
  );
}

export default App;
