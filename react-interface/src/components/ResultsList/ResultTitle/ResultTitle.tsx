import React from 'react';

import './ResultTitle.css';
import IconCopy from '../../../assets/icons/icon_copy.svg'


interface ResultTitleProps {
    children: string;
    isExpanded: boolean;
    toggleIsExpanded: () => void;
}

const ResultTitle: React.FC<ResultTitleProps> = ({ children, isExpanded, toggleIsExpanded }) => {

    return (
        <div className="result-title flex-row space-between">
            <div className="result-title-text mplus">{ children }</div>
            <div className="result-title-buttons flex-col space-between">
                <img
                    className="result-title-copy unselectable"
                    src={IconCopy}
                    alt="button to copy sample row to clipboard"
                />
                <div
                    className="result-title-collapser unselectable"
                    onClick={toggleIsExpanded}
                >
                    { isExpanded ? "collapse" : "expand" }
                </div>
            </div>
        </div>
    );
}

export default ResultTitle;
