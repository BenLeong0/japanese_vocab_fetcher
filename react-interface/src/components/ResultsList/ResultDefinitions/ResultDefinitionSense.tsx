import React from 'react';

import { JishoAPIItemSense } from '../../../types/ResponseItemJisho';

import UtilsService from '../../core/UtilsService';


interface ResultDefinitionSenseProps {
    ordinality: number;
    sense: JishoAPIItemSense;
}

const ResultDefinitionSense: React.FC<ResultDefinitionSenseProps> = ({ ordinality, sense }) => {
    const utilsService = new UtilsService();

    const dfn: string =
        ordinality + '. ' +
        sense.english_definitions.map(utilsService.capitaliseString).join("; ");

    const getWordType = (): string => {
        let wordType = sense.parts_of_speech.join("・");
        if (sense.tags.length > 0) {
            wordType += " (" + sense.tags.join(", ") + ")";
        }
        return wordType;
    }

    return (
        <div className="result-definition-sense flex-col">
            <div className="sense-part-of-speech">{ getWordType() }</div>
            <div className="sense-english-definition">{ dfn }</div>
        </div>
    );
}

export default ResultDefinitionSense;
