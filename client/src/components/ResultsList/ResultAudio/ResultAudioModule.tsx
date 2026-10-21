import React, { useState } from 'react';
import ResultAudioRow from './ResultAudioRow';

import ResultAudioRowData from '../../../types/ResultAudioRowData';


interface ResultAudioModuleProps {
    moduleTitle: string;
    audioData: ResultAudioRowData[];
}

const PREVIEW_ROWS = 3;

const ResultAudioModule: React.FC<ResultAudioModuleProps> = ({ moduleTitle, audioData}) => {
    const [isExpanded, setIsExpanded] = useState<boolean>(false);

    const canExpand = audioData.length > PREVIEW_ROWS;
    const visibleRows = isExpanded ? audioData : audioData.slice(0, PREVIEW_ROWS);

    return (
        <div className="audio-module">
            <span className="source-label">{ moduleTitle }</span>
            {visibleRows.map((audio, index) =>
                <ResultAudioRow key={`${audio.speaker}-${index}`} audioData={audio}/>
            )}
            { canExpand &&
                <button
                    type="button"
                    className="text-button"
                    onClick={() => setIsExpanded(!isExpanded)}
                >
                    {isExpanded ? "Show less" : `Show ${audioData.length - PREVIEW_ROWS} more`}
                </button>
            }
        </div>
    );
}

export default ResultAudioModule;
