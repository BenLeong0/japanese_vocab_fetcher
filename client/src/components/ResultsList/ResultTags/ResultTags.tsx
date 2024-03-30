import React from 'react';
import ResultTag from './ResultTag';

import FullResponseItem from '../../../types/FullResponseItem';

import './ResultTags.css'


interface ResultTagProps {
    data: FullResponseItem;
}

const ResultTags: React.FC<ResultTagProps> = ({ data }) => {
    const tags = extractTags(data);

    const displayTags = tags.length > 0;

    return (
        displayTags ?
        <div className="result-tags-container flex-row">
            {tags.map(tag =>
                <ResultTag key={tag} tag={tag} />
            )}
        </div> :
        <></>
    );
}


const extractTags = (data: FullResponseItem): string[] => {
    let tags = data.jisho.main_data.results.map(result => [result.jlpt, result.tags]).flat(2);
    if (data.jisho.main_data.results.some(result => result.is_common)) {
        tags.push("common word");
    }
    return tags;
}

export default ResultTags;
