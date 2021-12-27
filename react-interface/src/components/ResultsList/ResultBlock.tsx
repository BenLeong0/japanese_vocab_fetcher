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
        <div className="result-block flex-col">
            <ResultTitle>{ data.word }</ResultTitle>
            <div className="flex-row">
                <div className="result-left-col flex-col">
                    left
                </div>
                <div className="result-col-separator">&nbsp;</div>
                <div className="result-right-col flex-col">
                    right
                </div>
            </div>
        </div>
    );
}

export default Result;
