import React from 'react';
import ResultBlock from './ResultBlock'

import FullResponseItem from '../../types/FullResponseItem';

// import testWordList from './testWordList';
import './ResultsList.css'


interface ResultsListProps {
    wordList: FullResponseItem[];
}

const ResultsList: React.FC<ResultsListProps> = ({ wordList }) => {
    // TODO: Revert to not using testWordList

    return (
        <div className="results-list">
            {
                wordList.map(wordData =>
                    <ResultBlock key={wordData.word} data={wordData} />
                )
            }
        </div>
     );
}

export default ResultsList;
