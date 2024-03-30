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
            <div className="App">
                <div className="width-container">
                    <p className="app-header">Japanese Vocab Fetcher</p>
                    <InputPage setWordList={setWordList} />
                    <ResultsList wordList={wordList} />
                </div>
            </div>
        </BrowserRouter>
    );
}

export default App;
