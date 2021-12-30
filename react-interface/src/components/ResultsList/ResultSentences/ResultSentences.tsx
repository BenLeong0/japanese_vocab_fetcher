import React from 'react';
import ResultSentence from './ResultSentence';

import FullResponseItem from '../../../types/FullResponseItem';

import './ResultSentences.css';


interface ResultSentencesProps {
    data: FullResponseItem;
}

const ResultSentences: React.FC<ResultSentencesProps> = ({ data }) => {
    return (
        <div className="result-sentences flex-col">
            <div className="right-col-title">Context Sentences</div>
            <div className="result-sentences-container flex-col">
                {data.wanikani.main_data.sentences.map(sentence =>
                    <ResultSentence key={sentence.ja} sentence={sentence} source="Wanikani" />
                )}
            </div>
        </div>
    );
}

export default ResultSentences;
