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
    const japanesePodData: ResultAudioRowData[] = [{
        url: "https://audiostock-public-files.s3.ap-northeast-1.amazonaws.com/sample-files/demo_34d52dc1ec6ba4736f37c24458a2a7812e9b56f6.mp3",
        speaker: "Coming soon!",
        subtitle: null
    }]

    return (
        <div className="result-audio">
            <div className="left-col-title">
                Audio
            </div>
            <ResultAudioModule moduleTitle="Wanikani" audioData={wanikaniData} />
            <ResultAudioModule moduleTitle="Forvo" audioData={forvoData} />
            <ResultAudioModule moduleTitle="JapanesePod101" audioData={japanesePodData} />
        </div>
     );
}

export default ResultAudio;
