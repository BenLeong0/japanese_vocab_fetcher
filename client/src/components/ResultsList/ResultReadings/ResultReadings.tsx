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

const getJDictReadings = (data: FullResponseItem): string[] => {
    const readings = data.jdict.main_data.results.flatMap(entry => entry.readings);
    return Array.from(new Set(readings));
}

const ResultReadings: React.FC<ResultReadingsProps> = ({ data }) => {
    const sitesAndReadings: ReadingSite[] = [
        { title: "OJAD", readings: data.ojad.main_data.accent },
        { title: "Wadoku", readings: data.wadoku.main_data.accent },
        { title: "Suzuki", readings: data.suzuki.main_data.accent },
    ];

    const readingExists = ({ readings }: ReadingSite) => readings.length > 0;
    if (!sitesAndReadings.some(readingExists)) {
        // No pitch accent from any source: fall back to JMdict's plain (unaccented) readings
        sitesAndReadings.push({ title: "JMdict", readings: getJDictReadings(data) });
    }
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
