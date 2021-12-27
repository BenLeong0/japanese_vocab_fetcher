import React from 'react';

import FullResponseItem from '../../../types/FullResponseItem';

import './ResultTags.css'


interface ResultTagProps {
    data: FullResponseItem;
}

const ResultTags: React.FC<ResultTagProps> = ({ data }) => {
    const tags = extractTags(data);

    return ( <div className="result-tags-container flex-row">
        { tags.map(tag =>
            <div className="result-tag">{ tag }</div>
        )}
    </div> );
}


const extractTags = (data: FullResponseItem): string[] => {
    let tags: string[] = [];
    for (let result of data.jisho.main_data.results) {
        for (let jlptLevel of result.jlpt) {
            tags.push(jlptLevel.toUpperCase().replace("-", " "));
        }
        for (let tag of result.tags) {
            if (tag.slice(0, 8) === "wanikani") {
                tags.push(`Wanikani level ${tag.slice(8)}`);
            }
            else if (tag === "common-word") {
                tags.push("Common word");
            }
            else {
                tags.push(tag);
            }
        }
    }
    return tags;
}

export default ResultTags;
