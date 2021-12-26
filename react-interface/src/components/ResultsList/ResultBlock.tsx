import React from 'react';

import FullResponseItem from '../../types/FullResponseItem';
import ResultTitle from './ResultTitle/ResultTitle';

import './ResultBlock.css'


interface ResultProps {
    data: FullResponseItem;
}

const Result: React.FunctionComponent<ResultProps> = ({ data }) => {
    // const wanikaniData = data.wanikani;

    return (
        <div className="result-block">
            <ResultTitle>{ data.word }</ResultTitle>
        </div>
    );
}

export default Result;
