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

    const allAudio = [
        {module: "Wanikani", audioData: wanikaniData},
        {module: "Forvo", audioData: forvoData},
        {module: "JapanesePod101", audioData: japanesePodData},
    ]

    // TODO: Instate when JP101 is implemented
    // const displayAudio = (): boolean => {
    //     return allAudio.some(x => x.audioData.length > 0);
    // }

    const displayAudio = (): boolean => {
        return (
            wanikaniData.length > 0 ||
            forvoData.length > 0
        );
    }

    return (
        displayAudio() ?
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
