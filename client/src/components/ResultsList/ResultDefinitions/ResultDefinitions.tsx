import React from 'react';
import ResultDefinition from './ResultDefinition';
import Section from '../../../shared/Section/Section';

import FullResponseItem from '../../../types/FullResponseItem';


interface ResultDefinitionsProps {
    data: FullResponseItem;
}

const ResultDefinitions: React.FC<ResultDefinitionsProps> = ({ data }) => {
    if (data.jisho.main_data.results.length === 0) return null;

    return (
        <Section title="Definitions" className="section-definitions">
            <div className="definitions">
                { data.jisho.main_data.results.map(result =>
                    <ResultDefinition key={result.slug} definitionData={result} />
                )}
            </div>
        </Section>
    );
}

export default ResultDefinitions;
