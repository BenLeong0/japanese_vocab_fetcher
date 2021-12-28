import React, { useState } from 'react';
import ResultReadings from './ResultReadings/ResultReadings';
import ResultRelatedWords from './ResultRelatedWords/ResultRelatedWords';
import ResultTags from './ResultTags/ResultTags';
import ResultTitle from './ResultTitle/ResultTitle';
import ResultToggleBar from './ResultToggleBar/ResultToggleBar';

import FullResponseItem from '../../types/FullResponseItem';

import './ResultBlock.css';
import ResultAudio from './ResultAudio/ResultAudio';


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
                        <ResultReadings data={data} />
                        <ResultTags data={data} />
                        <ResultAudio data={data} />
                        <ResultRelatedWords data={data} />
                    </div>
                    <div className="result-col-separator" />
                    <div className="result-right-col flex-col">
                        right
                    </div>
                </div>
            }
            <ResultToggleBar isExpanded={isExpanded} toggleIsExpanded={toggleIsExpanded}/>
        </div>
    );
}

export default Result;
