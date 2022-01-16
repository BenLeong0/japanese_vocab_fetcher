import React from 'react';

import Sentence from '../../../types/Sentence';

import UtilsService from '../../core/UtilsService';

import { ReactComponent as IconCopy } from '../../../assets/icons/icon_copy.svg';


export interface ResultSentenceProps {
    sentence: Sentence;
    source: string;
}

const ResultSentence: React.FC<ResultSentenceProps> = ({ sentence, source }) => {
    const utilsService = new UtilsService();
    const copySentenceToClipboard = () => {
        utilsService.copyStringToClipboard(sentence.ja + '\t' + sentence.en);
    }

    return (
        <div className="result-sentence flex-col">
            <div className="result-sentence-top flex-row">
                <div className="result-sentence-ja">{ sentence.ja }</div>
                <div className="result-sentence-extra flex-row">
                    <div className="result-sentence-source">{ `- ${source}` }</div>
                    <IconCopy
                        className="result-sentence-copy"
                        onClick={copySentenceToClipboard}
                    />
                </div>
            </div>
            <div className="result-sentence-en">{ sentence.en }</div>
        </div>
    );
}

export default ResultSentence;
