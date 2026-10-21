import { useState } from 'react';
import { BrowserRouter } from "react-router-dom";
import InputPage from './components/InputPage/InputPage';
import ResultsList from './components/ResultsList/ResultsList';

import FullResponseItem from './types/FullResponseItem';

import './App.css';


function App() {
    const [wordList, setWordList] = useState<FullResponseItem[]>([]);

    return (
        <BrowserRouter>
            <div className="app">
                <header className="app-header">
                    <span className="app-mark" aria-hidden="true" />
                    <h1 className="app-title">Japanese Vocab Fetcher</h1>
                </header>
                <main>
                    <InputPage setWordList={setWordList} />
                    <ResultsList wordList={wordList} />
                </main>
            </div>
        </BrowserRouter>
    );
}

export default App;
