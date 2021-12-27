import React from 'react';

import FullResponseItem from '../../../types/FullResponseItem';
import ResultAudioRowData from '../../../types/ResultAudioRowData';

import './ResultAudio.css'
import ResultAudioModule from './ResultAudioModule';


interface ResultAudioProps {
    data: FullResponseItem;
}

const ResultAudio: React.FC<ResultAudioProps> = ({ data }) => {

    const wanikaniData: ResultAudioRowData[] = data.wanikani.main_data.audio.map(audio => ({
        url: audio.url,
        speaker: audio.metadata.voice_actor_name,
        subtitle: audio.metadata.voice_description,
    }))
    const forvoData: ResultAudioRowData[] = data.forvo.main_data.audio.map(audio => ({
        url: audio.url,
        speaker: audio.username,
        subtitle: null,
    }))

    return (
        <div className="result-audio">
            <div className="left-col-title">
                Audio
            </div>
            <ResultAudioModule moduleTitle="Wanikani" audioData={wanikaniData} />
            <ResultAudioModule moduleTitle="Forvo" audioData={forvoData} />
        </div>
     );
}

export default ResultAudio;
