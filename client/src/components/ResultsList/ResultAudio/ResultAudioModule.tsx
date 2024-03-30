import React, { useState } from 'react';
import FullExpandButton from '../../../shared/ExpandButtons/FullExpandButton';
import ResultAudioRow from './ResultAudioRow';

import ResultAudioRowData from '../../../types/ResultAudioRowData';


interface ResultAudioModuleProps {
    moduleTitle: string;
    audioData: ResultAudioRowData[];
}

const ResultAudioModule: React.FC<ResultAudioModuleProps> = ({ moduleTitle, audioData}) => {
    const [isExpanded, updateIsExpanded] = useState<boolean>(false);

    const displayButton = () => audioData.length > 3;
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
            { displayButton() &&
                <FullExpandButton
                    rowsDisplay={isExpanded}
                    updateRowsDisplay={updateIsExpanded}
                />
            }
        </div>
    );
}

export default ResultAudioModule;
