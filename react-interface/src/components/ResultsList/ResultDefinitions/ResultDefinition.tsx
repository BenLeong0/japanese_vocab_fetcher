import React from 'react';
import ResultDefinitionSense from './ResultDefinitionSense';

import { JishoAPIItem, JishoAPIItemJapanese } from '../../../types/ResponseItemJisho';


interface ResultDefinitionProps {
    definitionData: JishoAPIItem;
}

const ResultDefinition: React.FC<ResultDefinitionProps> = ({ definitionData }) => {
    const buildTitleText = (word: JishoAPIItemJapanese): string => {
        const main = word.word || word.reading || "";
        const subtext = word.word && word.reading && `【${word.reading}】`;
        return main + subtext;
    }

    return (
        <div className="result-definition flex-col">
            <div className="result-definition-title">
                { buildTitleText(definitionData.japanese[0]) }
            </div>
            <div className="result-definition-senses-container flex-col">
                { definitionData.senses.map((sense, index) =>
                    <ResultDefinitionSense key={index} ordinality={index+1} sense={sense} />
                )}
                {
                    definitionData.japanese.length > 1 &&
                    <div className="result-definition-other-forms">
                        <div className="result-other-forms-title">Other forms</div>
                        <div className="result-other-forms-words">
                            { definitionData.japanese.slice(1).map(buildTitleText).join("、") }
                        </div>
                    </div>
                }
            </div>
        </div>
    );
}

export default ResultDefinition;
