import React from 'react';
import ResultRelatedWord from './ResultRelatedWord';
import Section from '../../../shared/Section/Section';

import FullResponseItem from '../../../types/FullResponseItem';


interface ResultRelatedWordsProps {
    data: FullResponseItem;
}

const ResultRelatedWords: React.FC<ResultRelatedWordsProps> = ({ data }) => {
    if (data.jisho.main_data.extra.length === 0) return null;

    return (
        <Section title="Related words" className="section-related">
            <div className="chip-list">
                {data.jisho.main_data.extra.map(result =>
                    <ResultRelatedWord key={result.slug} relatedWord={result}/>
                )}
            </div>
        </Section>
     );
}

export default ResultRelatedWords;
