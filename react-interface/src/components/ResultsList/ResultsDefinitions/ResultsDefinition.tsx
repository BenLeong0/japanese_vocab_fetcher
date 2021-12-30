import React from 'react';

import { JishoAPIItem } from '../../../types/ResponseItemJisho';
import ResultsDefinitionSense from './ResultsDefinitionSense';


interface ResultsDefinitionProps {
    definitionData: JishoAPIItem;
}

const ResultsDefinition: React.FC<ResultsDefinitionProps> = ({ definitionData }) => {
    return (
        <div className="result-definition flex-col">
            <div className="result-definition-title">
                { definitionData.japanese[0].word || definitionData.japanese[0].reading}
                {
                    definitionData.japanese[0].word &&
                    definitionData.japanese[0].reading &&
                    `【${definitionData.japanese[0].reading}】`
                }
            </div>
            <div className="result-definition-senses-container flex-col">
                { definitionData.senses.map((sense, index) =>
                    <ResultsDefinitionSense key={index} ordinality={index+1} sense={sense} />
                )}
                {
                    definitionData.japanese.length > 1 &&
                    <div className="result-definition-other-forms">
                        <div className="result-other-forms-title">Other forms</div>
                        <div className="result-other-forms-words">
                            {
                                definitionData.japanese.slice(1).map(otherForm =>
                                    (otherForm.word || otherForm.reading || "") +
                                    (otherForm.word && otherForm.reading && `【${otherForm.reading}】`)
                                ).join("、")
                            }
                        </div>
                    </div>
                }
            </div>
        </div>
    );
}

export default ResultsDefinition;
