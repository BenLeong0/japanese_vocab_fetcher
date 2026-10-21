import React, { useState } from 'react';
import ExpandButton from '../../../shared/ExpandButtons/ExpandButton';
import ResultSentence, { ResultSentenceProps } from './ResultSentence';
import Section from '../../../shared/Section/Section';

import FullResponseItem from '../../../types/FullResponseItem';


interface ResultSentencesProps {
    data: FullResponseItem;
}

const ResultSentences: React.FC<ResultSentencesProps> = ({ data }) => {
    const wanikaniSentences: ResultSentenceProps[] =
        data.wanikani.main_data.sentences.map(s => ({sentence: s, source: "WaniKani"}));
    const tangorinSentences: ResultSentenceProps[] =
        data.tangorin.main_data.sentences.map(s => ({sentence: s, source: "Tangorin"}));

    const allSentences = interweaveSentences([
        wanikaniSentences,
        tangorinSentences,
    ]);

    const maxDisplay = allSentences.length;
    const minDisplay = Math.min(allSentences.length, 4);
    const [rowsDisplay, updateRowsDisplay] = useState<number>(minDisplay);

    if (allSentences.length === 0) return null;

    return (
        <Section title="Context sentences" className="section-sentences">
            <div className="sentences">
                {allSentences.slice(0, rowsDisplay).map(({ sentence, source }) =>
                    <ResultSentence key={sentence.ja} sentence={sentence} source={source} />
                )}
            </div>
            <ExpandButton
                currentDisplay={rowsDisplay}
                updateDisplay={updateRowsDisplay}
                maxDisplay={maxDisplay}
                minDisplay={minDisplay}
                batchSize={4}
            />
        </Section>
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
