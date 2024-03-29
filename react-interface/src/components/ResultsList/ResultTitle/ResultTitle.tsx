import React from 'react';

import IconCopy from '../../../assets/icons/icon_copy.svg';

import UtilsService from '../../core/UtilsService';

import './ResultTitle.css';


interface ResultTitleProps {
    children: string;
    isExpanded: boolean;
    toggleIsExpanded: () => void;
    copyString: string;
}

const ResultTitle: React.FC<ResultTitleProps> = ({
    children,
    isExpanded,
    toggleIsExpanded,
    copyString,
}) => {
    const utilsService = new UtilsService();
    const copyCopyStringToClipboard = () => {
        utilsService.copyStringToClipboard(copyString);
    }

    return (
        <div className="result-title flex-row space-between">
            <div className="result-title-text mplus">{ children }</div>
            <div className="result-title-buttons flex-col space-between">
                <img
                    className="result-title-copy unselectable"
                    src={IconCopy}
                    alt="button to copy sample row to clipboard"
                    onClick={copyCopyStringToClipboard}
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
