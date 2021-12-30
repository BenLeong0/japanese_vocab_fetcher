import React from 'react';

import './ResultTitle.css'


interface ResultTitleProps {
    children: string;
    isExpanded: boolean;
    toggleIsExpanded: () => void;
}

const ResultTitle: React.FC<ResultTitleProps> = ({ children, isExpanded, toggleIsExpanded }) => {

    return (
        <div className="result-title">
            { children }
            <div
                className="title-collapser"
                onClick={toggleIsExpanded}
            >
                { isExpanded ? "collapse" : "expand" }
            </div>
        </div>
    );
}

export default ResultTitle;
