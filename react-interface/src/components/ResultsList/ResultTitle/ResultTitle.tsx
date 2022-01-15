import React from 'react';

import './ResultTitle.css';


interface ResultTitleProps {
    children: string;
    isExpanded: boolean;
    toggleIsExpanded: () => void;
}

const ResultTitle: React.FC<ResultTitleProps> = ({ children, isExpanded, toggleIsExpanded }) => {

    return (
        <div className="result-title">
            <div className="result-title-text">{ children }</div>
            <div
                className="title-collapser unselectable"
                onClick={toggleIsExpanded}
            >
                { isExpanded ? "collapse" : "expand" }
            </div>
        </div>
    );
}

export default ResultTitle;
