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

    const displayRow = (rowIndex: number): boolean => {
        return (
            rowIndex < 2 ||
            (rowIndex === 2 && audioData.length === 3) ||
            isExpanded === true
        );
    }

    return (
        <div className="result-audio-module vertical-separation-small">
            <div className="audio-module-title">{ moduleTitle }</div>
            {audioData.filter((_, rowIndex) => displayRow(rowIndex)).map(audio =>
                <ResultAudioRow key={audio.speaker} audioData={audio}/>
            )}
            {audioData.length > 3 &&
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
