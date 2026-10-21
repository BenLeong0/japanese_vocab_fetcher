import React from 'react';
import ResultAudioModule from './ResultAudioModule';
import Section from '../../../shared/Section/Section';

import FullResponseItem from '../../../types/FullResponseItem';
import ResultAudioRowData from '../../../types/ResultAudioRowData';


interface ResultAudioProps {
    data: FullResponseItem;
}

interface AudioModule {
    module: string;
    audioData: ResultAudioRowData[];
}

const ResultAudio: React.FC<ResultAudioProps> = ({ data }) => {
    const wanikaniData: ResultAudioRowData[] = data.wanikani.main_data.audio.map(audio => ({
        url: audio.url,
        speaker: audio.metadata.voice_actor_name,
        subtitle: audio.metadata.voice_description,
    }));
    const forvoData: ResultAudioRowData[] = data.forvo.main_data.audio.map(audio => ({
        url: audio.url,
        speaker: audio.username,
        subtitle: null,
    }));
    const japanesePodData: ResultAudioRowData[] = data.japanesepod.main_data.audio.map(audio => ({
        url: audio.url,
        speaker: audio.writing,
        subtitle: audio.reading,
    }));

    const allAudio: AudioModule[] = [
        {module: "WaniKani", audioData: wanikaniData},
        {module: "Forvo", audioData: forvoData},
        {module: "JapanesePod101", audioData: japanesePodData},
    ].filter(({ audioData }) => audioData.length > 0);

    if (allAudio.length === 0) return null;

    return (
        <Section title="Audio" className="section-audio">
            {allAudio.map(({ module, audioData }) =>
                <ResultAudioModule key={module} moduleTitle={module} audioData={audioData} />
            )}
        </Section>
     );
}

export default ResultAudio;
