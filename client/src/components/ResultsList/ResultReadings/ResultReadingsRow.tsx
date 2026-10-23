import React from 'react';

import UtilsService from '../../core/UtilsService';


interface ResultReadingsRowProps {
    title: string;
    readings: string[];
}

const ResultReadingsRow: React.FC<ResultReadingsRowProps> = ({ title, readings }) => {
    const utilsService = new UtilsService();

    return (
        <div className="readings-row">
            <span className="source-label">{ title }</span>
            <div className="readings-list">
                {readings.map((reading, index) =>
                    <button
                        key={index}
                        type="button"
                        className="chip chip-copy ja"
                        onClick={() => utilsService.copyStringToClipboard(reading)}
                        title="Copy to clipboard"
                    >{ reading }</button>
                )}
            </div>
        </div>
     );
}

export default ResultReadingsRow;
