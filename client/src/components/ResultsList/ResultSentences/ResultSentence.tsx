import React from 'react';
import CopyButton from '../../../shared/CopyButton/CopyButton';

import Sentence from '../../../types/Sentence';


export interface ResultSentenceProps {
    sentence: Sentence;
    source: string;
}

const ResultSentence: React.FC<ResultSentenceProps> = ({ sentence, source }) => {
    return (
        <div className="sentence">
            <div className="sentence-text">
                <p className="sentence-ja ja">{ sentence.ja }</p>
                <p className="sentence-en">{ sentence.en }</p>
                <span className="source-label">{ source }</span>
            </div>
            <CopyButton text={`${sentence.ja}\t${sentence.en}`} label="Copy sentence" />
        </div>
    );
}

export default ResultSentence;
