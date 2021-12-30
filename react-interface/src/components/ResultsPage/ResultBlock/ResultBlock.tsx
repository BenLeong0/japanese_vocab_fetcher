import React, { FunctionComponent } from 'react';

import FullResponseItem from '../../../types/FullResponseItem';


interface ResultProps {
    data: FullResponseItem;
}

const Result: FunctionComponent<ResultProps> = ({ data }) => {
    const wanikaniData = data.wanikani;

    return ( <>{wanikaniData.main_data.sentences[0].en}</> );
}

export default Result;
