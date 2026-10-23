import React from 'react';
import ResultTag from './ResultTag';
import Section from '../../../shared/Section/Section';

import FullResponseItem from '../../../types/FullResponseItem';


interface ResultTagProps {
    data: FullResponseItem;
}

const ResultTags: React.FC<ResultTagProps> = ({ data }) => {
    const tags = extractTags(data);
    if (tags.length === 0) return null;

    return (
        <Section title="Tags" className="section-tags">
            <div className="chip-list">
                {tags.map(tag =>
                    <ResultTag key={tag} tag={tag} />
                )}
            </div>
        </Section>
    );
}


const extractTags = (data: FullResponseItem): string[] => {
    let tags = data.jisho.main_data.results.map(result => [result.jlpt, result.tags]).flat(2);
    if (data.jisho.main_data.results.some(result => result.is_common)
        || data.jdict.main_data.results.some(result => result.is_common)) {
        tags.push("common word");
    }
    return Array.from(new Set(tags));
}

export default ResultTags;
