import React from 'react';

import FullResponseItem from '../../types/FullResponseItem';

import ResultBlock from './ResultBlock/ResultBlock'


interface ResultsPageProps {
    wordList: FullResponseItem[];
}

const ResultsPage: React.FC<ResultsPageProps> = ({ wordList }) => {
    return (
        <>
            {
                wordList.map(wordData =>
                    <ResultBlock data={wordData} />
                )
            }
        </>
     );
}

export default ResultsPage;
