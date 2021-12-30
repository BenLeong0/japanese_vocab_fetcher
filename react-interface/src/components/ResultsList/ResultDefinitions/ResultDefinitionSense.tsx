import React from 'react';

import { JishoAPIItemSense } from '../../../types/ResponseItemJisho';


interface ResultDefinitionSenseProps {
    ordinality: number;
    sense: JishoAPIItemSense;
}

const ResultDefinitionSense: React.FC<ResultDefinitionSenseProps> = ({ ordinality, sense }) => {

    const dfn = ordinality + '. ' + sense.english_definitions.join("; ");

    const getWordType = () => {
        let wordType = sense.parts_of_speech.join(", ");
        if (sense.tags.length > 0) {
            wordType += " (" + sense.tags.join(", ") + ")";
        }
        return wordType
    }

    return (
        <div className="result-definition-sense flex-col">
            <div className="sense-part-of-speech">{ getWordType() }</div>
            <div className="sense-english-definition">{ dfn }</div>
        </div>
    );
}

export default ResultDefinitionSense;
