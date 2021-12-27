import React from 'react';

import FullResponseItem from '../../../types/FullResponseItem';

import './ResultReadings.css'
import ResultsReadingsRow from './ResultReadingsRow';


interface ResultReadingsProps {
    data: FullResponseItem;
}

const ResultReadings: React.FC<ResultReadingsProps> = ({ data }) => {
    const sitesAndReadings = [
        { title: "OJAD", readings: data.ojad.main_data.accent},
        { title: "Wadoku", readings: data.wadoku.main_data.accent},
        { title: "Suzuki", readings: data.suzuki.main_data.accent},
    ]

    return (
        <div className="result-readings">
            <div className="readings-title">
                Readings
            </div>
            {sitesAndReadings.map(({title, readings}) =>
                <ResultsReadingsRow title={title} readings={readings} />
            )}
        </div>
     );
}

export default ResultReadings;
