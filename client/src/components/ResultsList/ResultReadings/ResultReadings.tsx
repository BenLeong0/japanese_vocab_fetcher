import React from 'react';
import ResultReadingsRow from './ResultReadingsRow';
import Section from '../../../shared/Section/Section';

import FullResponseItem from '../../../types/FullResponseItem';


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

    const readingExists = ({ readings }: ReadingSite) => readings.length > 0;
    if (!sitesAndReadings.some(readingExists)) return null;

    return (
        <Section title="Readings" className="section-readings">
            {sitesAndReadings.filter(readingExists).map(({ title, readings }) =>
                <ResultReadingsRow key={title} title={title} readings={readings} />
            )}
        </Section>
     );
}

export default ResultReadings;
