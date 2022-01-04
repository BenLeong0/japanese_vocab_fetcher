import React from 'react';


interface ResultTagProps {
    tag: string;
}

const ResultTag: React.FC<ResultTagProps> = ({ tag }) => {
    const translatedTag = (
        tag.slice(0,8) === "wanikani" ?
        `wanikani level ${tag.slice(8)}` :
        tag.toLowerCase().replace("-", " ")
    );

    return <div className="result-tag">{ translatedTag }</div> ;
}



export default ResultTag;
