import React, { useState } from 'react';

import FullResponseItem from '../../types/FullResponseItem';
import ResultTitle from './ResultTitle/ResultTitle';

import './ResultBlock.css'


interface ResultProps {
    data: FullResponseItem;
}

const Result: React.FunctionComponent<ResultProps> = ({ data }) => {
    const [isExpanded, setIsExpanded] = useState<boolean>(true);
    const toggleIsExpanded = () => setIsExpanded(!isExpanded);

    // const wanikaniData = data.wanikani;

    return (
        <div className="result-block flex-col">
            <ResultTitle
                isExpanded={isExpanded}
                toggleIsExpanded={toggleIsExpanded}
            >{ data.word }</ResultTitle>
            { isExpanded &&
                <div className="flex-row">
                    <div className="result-left-col flex-col">
                        left
                    </div>
                    <div className="result-col-separator" />
                    <div className="result-right-col flex-col">
                        right
                    </div>
                </div>
            }
        </div>
    );
}

export default Result;
