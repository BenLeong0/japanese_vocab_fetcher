import React from 'react';
import ResultAudioRow from './ResultAudioRow';

import ResultAudioRowData from '../../../types/ResultAudioRowData';


interface ResultAudioModuleProps {
    moduleTitle: string;
    audioData: ResultAudioRowData[];
}

const ResultAudioModule: React.FC<ResultAudioModuleProps> = ({ moduleTitle, audioData}) => {
    return (
        <div className="result-audio-module">
            <div className="audio-module-title">{ moduleTitle }</div>
            {audioData.map(audio =>
                <ResultAudioRow key={audio.speaker} audioData={audio}/>
            )}
        </div>
    );
}

export default ResultAudioModule;
