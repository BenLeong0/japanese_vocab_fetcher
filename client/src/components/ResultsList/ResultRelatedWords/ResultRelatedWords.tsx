import React from 'react';
import ResultRelatedWord from './ResultRelatedWord';

import FullResponseItem from '../../../types/FullResponseItem';

import './ResultRelatedWords.css';


interface ResultRelatedWordsProps {
    data: FullResponseItem;
}

const ResultRelatedWords: React.FC<ResultRelatedWordsProps> = ({ data }) => {
    const displayRelatedWords = (): boolean => {
        return data.jisho.main_data.extra.length > 0;
    }

    return (
        displayRelatedWords() ?
        <div className="result-related-words vertical-separation-small">
            <div className="left-col-title">
                Related words
            </div>
            <div className="related-words-container flex-row">
                {data.jisho.main_data.extra.map(result =>
                    <ResultRelatedWord key={result.slug} relatedWord={result}/>
                )}
            </div>
        </div> :
        <></>
     );
}

export default ResultRelatedWords;
