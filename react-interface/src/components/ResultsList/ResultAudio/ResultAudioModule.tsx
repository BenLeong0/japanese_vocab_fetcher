import React from 'react';

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
                <div className="result-audio">
                    <img src={ audio.url } alt="audio player icon" className="audio-player" />
                    <div className="result-audio-speaker">{ audio.speaker }</div>
                    <div className="result-audio-subtitle">{ audio.subtitle }</div>
                </div>
            )}
        </div>
    );
}

export default ResultAudioModule;
