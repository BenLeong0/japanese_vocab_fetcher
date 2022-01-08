import React from 'react';
import ResultSentence, { ResultSentenceProps } from './ResultSentence';

import FullResponseItem from '../../../types/FullResponseItem';

import './ResultSentences.css';


interface ResultSentencesProps {
    data: FullResponseItem;
}

const ResultSentences: React.FC<ResultSentencesProps> = ({ data }) => {
    const wanikaniSentences: ResultSentenceProps[] = data.wanikani.main_data.sentences.map(s => ({sentence: s, source: "Wanikani"}));
    const tangorinSentences: ResultSentenceProps[] = data.tangorin.main_data.sentences.map(s => ({sentence: s, source: "Tangorin"}));

    const allSentences = interweaveSentences([
        wanikaniSentences,
        tangorinSentences,
    ]);

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

const interweaveSentences = (sentenceLists: ResultSentenceProps[][]): ResultSentenceProps[] => {
    const maxLength = Math.max(...sentenceLists.map(list => list.length));
    let finalList: ResultSentenceProps[] = [];
    for (let i = 0; i < maxLength; i++) {
        for (let sentenceList of sentenceLists) {
            if (i < sentenceList.length) {
                finalList.push(sentenceList[i]);
            }
        }
    }
    return finalList;
}

export default ResultSentences;
