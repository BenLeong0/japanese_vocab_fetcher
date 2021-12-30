import React from 'react';

import { JishoAPIItemSense } from '../../../types/ResponseItemJisho';


interface ResultDefinitionSenseProps {
    ordinality: number;
    sense: JishoAPIItemSense;
}

const ResultsDefinitionSense: React.FC<ResultDefinitionSenseProps> = ({ ordinality, sense}) => {
    return (
        <div className="result-definition-sense flex-col">
            <div className="sense-part-of-speech">{
                sense.parts_of_speech.join(", ") +
                (sense.tags.length > 0 ? " (" + sense.tags.join(", ") + ")" : "")
            }</div>
            <div className="sense-english-definition">
                { ordinality }. {sense.english_definitions.join("; ")}
            </div>
        </div>
    );
}

export default ResultsDefinitionSense;
