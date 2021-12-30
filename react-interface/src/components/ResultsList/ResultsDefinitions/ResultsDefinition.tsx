import React from 'react';


import { JishoAPIItem } from '../../../types/ResponseItemJisho';


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
            { definitionData.japanese[0].word || definitionData.japanese[0].reading}
        </div>
    );
}

export default ResultsDefinition;
