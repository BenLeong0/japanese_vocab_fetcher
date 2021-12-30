import React from 'react';
import ResultDefinition from './ResultDefinition';

import FullResponseItem from '../../../types/FullResponseItem';

import './ResultDefinitions.css';


interface ResultDefinitionsProps {
    data: FullResponseItem;
}

const ResultDefinitions: React.FC<ResultDefinitionsProps> = ({ data }) => {
    return (
        <div className="result-definitions-container flex-col">
            { data.jisho.main_data.results.map(result =>
                <ResultDefinition key={result.slug} definitionData={result} />
            )}
        </div>
    );
}

export default ResultDefinitions;
