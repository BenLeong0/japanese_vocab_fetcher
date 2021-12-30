import { useState } from 'react';
import InputPage from './components/InputPage/InputPage';
import ResultsPage from './components/ResultsPage/ResultsPage';

import FullResponseItem from './types/FullResponseItem';

import './App.css';


function App() {
    const [wordList, setWordList] = useState<FullResponseItem[]>([]);

    return (
        <div className="App">
            <div className="width-container">
                <p className="app-header">Japanese Vocab Fetcher</p>
                <InputPage setWordList={setWordList} />
                <ResultsPage wordList={wordList} />
            </div>
        </div>
    );
}

export default App;
