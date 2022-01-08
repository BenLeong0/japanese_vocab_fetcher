import React, { useState } from 'react';
import ExpandButton from '../../../shared/ExpandButtons/ExpandButton';
import ResultAudioRow from './ResultAudioRow';

import ResultAudioRowData from '../../../types/ResultAudioRowData';


interface ResultAudioModuleProps {
    moduleTitle: string;
    audioData: ResultAudioRowData[];
}

const ResultAudioModule: React.FC<ResultAudioModuleProps> = ({ moduleTitle, audioData}) => {
    const maxDisplay = audioData.length;
    const minDisplay = audioData.length <= 3 ? audioData.length : 2;
    const [rowsDisplay, updateRowsDisplay] = useState<number>(minDisplay);

    const displayRow = (rowIndex: number): boolean => rowIndex+1 <= rowsDisplay;

    return (
        <div className="result-audio-module vertical-separation-small">
            <div className="audio-module-title">{ moduleTitle }</div>
            {audioData.filter((_, rowIndex) => displayRow(rowIndex)).map(audio =>
                <ResultAudioRow key={audio.speaker} audioData={audio}/>
            )}
            <div className="expand-button-container">
                <ExpandButton
                    currentDisplay={rowsDisplay}
                    updateDisplay={updateRowsDisplay}
                    maxDisplay={maxDisplay}
                    minDisplay={minDisplay}
                    batchSize={999}
                />
            </div>
        </div>
    );
}

export default ResultAudioModule;
