import React from 'react';

import FullResponseItem from '../../../types/FullResponseItem';

import './ResultReadings.css';
import ResultReadingsRow from './ResultReadingsRow';


interface ResultReadingsProps {
    data: FullResponseItem;
}

interface ReadingSite {
    title: string;
    readings: string[];
}

const ResultReadings: React.FC<ResultReadingsProps> = ({ data }) => {
    const sitesAndReadings: ReadingSite[] = [
        { title: "OJAD", readings: data.ojad.main_data.accent },
        { title: "Wadoku", readings: data.wadoku.main_data.accent },
        { title: "Suzuki", readings: data.suzuki.main_data.accent },
    ];

    const displayReadings = (): boolean => sitesAndReadings.some(site => site.readings.length > 0);
    const readingExists = ({ readings }: ReadingSite) => readings.length > 0;

    return (
        displayReadings() ?
        <div className="result-readings">
            <div className="left-col-title">
                Readings
            </div>
            {sitesAndReadings.filter(readingExists).map(({ title, readings }) =>
                <ResultReadingsRow key={title} title={title} readings={readings} />
            )}
        </div> :
        <></>
     );
}

export default ResultReadings;
