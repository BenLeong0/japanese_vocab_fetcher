import React from 'react';


interface ResultTagProps {
    tag: string;
}

const ResultTag: React.FC<ResultTagProps> = ({ tag }) => {
    const isCommon = tag === "common word";
    const translatedTag = (
        tag.slice(0,8) === "wanikani" ?
        `WaniKani level ${tag.slice(8)}` :
        tag.slice(0,5) === "jlpt-" ?
        `JLPT ${tag.slice(5).toUpperCase()}` :
        tag.toLowerCase().replace("-", " ")
    );

    return <span className={`chip ${isCommon ? "chip-accent" : ""}`}>{ translatedTag }</span>;
}

export default ResultTag;
