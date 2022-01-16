import React from 'react';

import UtilsService from '../../core/UtilsService';


interface ResultReadingsRowProps {
    title: string;
    readings: string[];
}

const ResultReadingsRow: React.FC<ResultReadingsRowProps> = ({ title, readings }) => {
    const utilsService = new UtilsService();
    const copyReadingToClipboard = (reading: string) => {
        utilsService.copyStringToClipboard(reading);
    }

    return (
        <div className="readings-row">
            <div className="readings-row-left unselectable">{ title }:</div>
            <div className="readings-row-right">
                {readings.map((reading, index) =>
                    <div
                        key={index}
                        className="reading unselectable"
                        onClick={() => {copyReadingToClipboard(reading)}}
                        title="Copy to clipboard"
                    >{ reading }</div>
                )}
            </div>
        </div>
     );
}

export default ResultReadingsRow;
