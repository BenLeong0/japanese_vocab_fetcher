import React from 'react';
import ResultBlock from './ResultBlock'

import FullResponseItem from '../../types/FullResponseItem';

import './ResultsList.css'


interface ResultsListProps {
    wordList: FullResponseItem[];
}

const ResultsList: React.FC<ResultsListProps> = ({ wordList }) => {
    return (
        <div className="results-list">
            {
                wordList.map(wordData =>
                    <ResultBlock data={wordData} />
                )
            }
        </div>
     );
}

export default ResultsList;
