import React from 'react';

import { JishoAPIItemSense } from '../../../types/ResponseItemJisho';

import UtilsService from '../../core/UtilsService';


interface ResultDefinitionSenseProps {
    ordinality: number;
    sense: JishoAPIItemSense;
}

const ResultDefinitionSense: React.FC<ResultDefinitionSenseProps> = ({ ordinality, sense }) => {
    const utilsService = new UtilsService();

    const dfn: string = sense.english_definitions.map(utilsService.capitaliseString).join(" ; ");

    const getWordType = (): string => {
        let wordType = sense.parts_of_speech.join("・");
        if (sense.tags.length > 0) {
            wordType += " (" + sense.tags.join(", ") + ")";
        }
        if (sense.info.length > 0) {
            wordType += " (" + sense.info.join(", ") + ")";
        }
        return wordType;
    }

    return (
        <div className="sense">
            { getWordType() && <div className="sense-pos">{ getWordType() }</div> }
            <div className="sense-text">
                <span
                    className="sense-ordinal unselectable"
                    title="Copy definition"
                    onClick={() => utilsService.copyStringToClipboard(dfn)}
                >{ ordinality }.</span>
                { dfn }
            </div>
        </div>
    );
}

export default ResultDefinitionSense;
