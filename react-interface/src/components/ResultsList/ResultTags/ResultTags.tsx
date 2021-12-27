import React from 'react';
import ResultTag from './ResultTag';

import FullResponseItem from '../../../types/FullResponseItem';

import './ResultTags.css'


interface ResultTagProps {
    data: FullResponseItem;
}

const ResultTags: React.FC<ResultTagProps> = ({ data }) => {
    const tags = extractTags(data);

    return ( <div className="result-tags-container flex-row">
        { tags.map(tag =>
            <ResultTag tag={tag} />
        )}
    </div> );
}


const extractTags = (data: FullResponseItem): string[] => {
    return data.jisho.main_data.results.map(result => [result.jlpt, result.tags]).flat(2);
}

export default ResultTags;
