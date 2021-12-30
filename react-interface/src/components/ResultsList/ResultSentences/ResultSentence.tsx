import React from 'react';

import Sentence from '../../../types/Sentence';


interface ResultSentenceProps {
    sentence: Sentence;
    source: string;
}

const ResultSentence: React.FC<ResultSentenceProps> = ({ sentence, source }) => {
    return (
        <div className="result-sentence flex-col">
            <div className="result-sentence-top flex-row">
                <div className="result-sentence-ja">{ sentence.ja }</div>
                <div className="result-sentence-source">- { source }</div>
            </div>
            <div className="result-sentence-en">{ sentence.en }</div>
        </div>
    );
}

export default ResultSentence;
