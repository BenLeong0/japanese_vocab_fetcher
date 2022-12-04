import React from 'react';
import ResultAudioModule from './ResultAudioModule';

import FullResponseItem from '../../../types/FullResponseItem';
import ResultAudioRowData from '../../../types/ResultAudioRowData';

import './ResultAudio.css';


interface ResultAudioProps {
    data: FullResponseItem;
}

interface AudioModule {
    module: string;
    audioData: ResultAudioRowData[];
}

const ResultAudio: React.FC<ResultAudioProps> = ({ data }) => {
    const wanikaniData: ResultAudioRowData[] = data.wanikani.main_data.audio.map((audio) => ({
        url: audio.url,
        speaker: audio.metadata.voice_actor_name,
        subtitle: audio.metadata.voice_description,
    }));
    const forvoData: ResultAudioRowData[] = data.forvo.main_data.audio.map((audio) => ({
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
        { module: "Wanikani", audioData: wanikaniData },
        { module: "Forvo", audioData: forvoData },
        { module: "JapanesePod101", audioData: japanesePodData },
    ];

    const displayAudio = (): boolean => allAudio.some(x => x.audioData.length > 0);

    return ( displayAudio() ?
        <div className="result-audio">
            <div className="left-col-title">
                Audio
            </div>
            {allAudio.filter(({ audioData }) => audioData.length > 0).map(({ module, audioData }) =>
                <ResultAudioModule key={module} moduleTitle={module} audioData={audioData} />
            )}
        </div> :
        <></>
    );
}

export default ResultAudio;
