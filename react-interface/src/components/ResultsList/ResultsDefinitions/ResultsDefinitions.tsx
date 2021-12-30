import React from 'react';

import FullResponseItem from '../../../types/FullResponseItem';
import ResultsDefinition from './ResultsDefinition';

import './ResultsDefinitions.css'


interface ResultsDefinitionsProps {
    data: FullResponseItem;
}

const ResultsDefinitions: React.FC<ResultsDefinitionsProps> = ({ data }) => {
    return (
        <div className="result-definitions-container flex-col">
            { data.jisho.main_data.results.map(result =>
                <ResultsDefinition key={result.slug} definitionData={result} />
            )}
        </div>
    );
}

export default ResultsDefinitions;
