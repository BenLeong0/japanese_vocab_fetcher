import React, { useState } from 'react';
import ResultAudioRow from './ResultAudioRow';

import ResultAudioRowData from '../../../types/ResultAudioRowData';

import IconPlus from '../../../assets/icons/icon_plus.svg'
import IconMinus from '../../../assets/icons/icon_minus.svg'


interface ResultAudioModuleProps {
    moduleTitle: string;
    audioData: ResultAudioRowData[];
}

const ResultAudioModule: React.FC<ResultAudioModuleProps> = ({ moduleTitle, audioData}) => {
    const [isExpanded, setIsExpanded] = useState<boolean>(false);
    const toggleIsExpanded = () => setIsExpanded(!isExpanded);

    return (
        <div className="result-audio-module">
            <div className="audio-module-title">{ moduleTitle }</div>
            {audioData.map((audio, rowIndex) =>
                <ResultAudioRow key={audio.speaker} rowIndex={rowIndex} audioData={audio} isExpanded={isExpanded}/>
            )}
            {audioData.length > 2 &&
                <div className="audio-expand-toggle" onClick={toggleIsExpanded}>
                    <img
                        src={isExpanded ? IconMinus : IconPlus}
                        alt="button to toggle expanded list of audio files"
                    />
                </div>
            }
        </div>
    );
}

export default ResultAudioModule;
