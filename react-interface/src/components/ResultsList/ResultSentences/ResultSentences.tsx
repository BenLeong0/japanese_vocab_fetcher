import React from 'react';
import ResultSentence from './ResultSentence';

import FullResponseItem from '../../../types/FullResponseItem';

import './ResultSentences.css';


interface ResultSentencesProps {
    data: FullResponseItem;
}

const ResultSentences: React.FC<ResultSentencesProps> = ({ data }) => {
    const allSentences = [
        ...data.wanikani.main_data.sentences.map(s => ({sentence: s, source: "Wanikani"})),
    ];

    return (
        allSentences.length > 0 ?
        <div className="result-sentences flex-col">
            <div className="right-col-title">Context Sentences</div>
            <div className="result-sentences-container flex-col">
                {allSentences.map(({ sentence, source }) =>
                    <ResultSentence key={sentence.ja} sentence={sentence} source={source} />
                )}
            </div>
        </div> :
        <></>
    );
}

export default ResultSentences;
