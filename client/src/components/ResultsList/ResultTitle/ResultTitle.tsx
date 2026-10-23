import React from 'react';
import CopyButton from '../../../shared/CopyButton/CopyButton';
import { IconChevron } from '../../../shared/Icons/Icons';


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
    return (
        <header className="result-header">
            <h2 className="result-word ja">{ children }</h2>
            <div className="result-actions">
                <CopyButton text={copyString} label="Copy row to clipboard" />
                <button
                    type="button"
                    className="icon-button"
                    title={isExpanded ? "Collapse" : "Expand"}
                    aria-label={isExpanded ? "Collapse" : "Expand"}
                    aria-expanded={isExpanded}
                    onClick={toggleIsExpanded}
                >
                    <IconChevron up={isExpanded} />
                </button>
            </div>
        </header>
    );
}

export default ResultTitle;
