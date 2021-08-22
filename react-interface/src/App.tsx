import React from 'react';
import './App.css';
import InputPage from './components/InputPage/InputPage';

function App() {
  return (
    <div className="App">
      <div className="width-container">
        <p className="app-header">Japanese Vocab Fetcher</p>
        <InputPage />
      </div>
    </div>
  );
}

export default App;
