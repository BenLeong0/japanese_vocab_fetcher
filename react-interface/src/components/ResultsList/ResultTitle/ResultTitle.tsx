import React, { useState } from 'react';

import './ResultTitle.css'


interface ResultTitleProps {
    children: string;
}

const ResultTitle: React.FunctionComponent<ResultTitleProps> = ({ children }) => {
    const [isExpanded, setIsExpanded] = useState<boolean>(true);
    const toggleState = () => setIsExpanded(!isExpanded)

    return (
        <div className="result-title">
            { children }
            <div
                className="title-collapser"
                onClick={toggleState}
            >{ isExpanded ? "collapse" : "expand" }</div>
        </div>
    );
}

export default ResultTitle;
