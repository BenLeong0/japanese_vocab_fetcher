import React from 'react';
import ResultDefinition from './ResultDefinition';
import ResultJDictDefinition from './ResultJDictDefinition';
import Section from '../../../shared/Section/Section';

import FullResponseItem from '../../../types/FullResponseItem';


interface ResultDefinitionsProps {
    data: FullResponseItem;
}

const ResultDefinitions: React.FC<ResultDefinitionsProps> = ({ data }) => {
    const jishoResults = data.jisho.main_data.results;
    const jdictResults = data.jdict.main_data.results;
    if (jishoResults.length === 0 && jdictResults.length === 0) return null;

    return (
        <Section title="Definitions" className="section-definitions">
            { jishoResults.length > 0 &&
                <div className="definitions">
                    { jdictResults.length > 0 && <div className="definitions-source">Jisho</div> }
                    { jishoResults.map(result =>
                        <ResultDefinition key={result.slug} definitionData={result} />
                    )}
                </div>
            }
            { jdictResults.length > 0 &&
                <div className="definitions">
                    <div className="definitions-source">JMdict (WWWJDIC)</div>
                    { jdictResults.map((entry, index) =>
                        <ResultJDictDefinition key={index} entry={entry} />
                    )}
                </div>
            }
        </Section>
    );
}

export default ResultDefinitions;
