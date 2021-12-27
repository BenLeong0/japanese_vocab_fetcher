import React from 'react';

import FullResponseItem from '../../../types/FullResponseItem';


interface ResultTagProps {
    data: FullResponseItem;
}

const ResultTag: React.FC<ResultTagProps> = ({ data }) => {

    return ( <>
        { data.jisho.main_data.results.map(result => result.tags.map(tag =>
            <div className="result-tag">{ tag }</div>
        ))}
    </> );
}

export default ResultTag;
