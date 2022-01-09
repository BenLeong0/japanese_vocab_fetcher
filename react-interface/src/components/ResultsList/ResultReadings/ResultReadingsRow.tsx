import React from 'react';


interface ResultReadingsRowProps {
    title: string;
    readings: string[];
}

const ResultReadingsRow: React.FC<ResultReadingsRowProps> = ({ title, readings }) => {
    return (
        <div className="readings-row">
            <div className="readings-row-left">{ title }:</div>
            <div className="readings-row-right">
                {readings.map((reading, index) =>
                    <div key={index} className="reading">{ reading }</div>
                )}
            </div>
        </div>
     );
}

export default ResultReadingsRow;
