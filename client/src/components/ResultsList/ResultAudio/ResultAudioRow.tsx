import React, { useState, useEffect } from 'react';
import { IconPlay, IconStop } from '../../../shared/Icons/Icons';

import ResultAudioRowData from '../../../types/ResultAudioRowData';


interface ResultAudioRowProps {
    audioData: ResultAudioRowData;
}

const ResultAudioRow: React.FC<ResultAudioRowProps> = ({ audioData }) => {
    const [audio] = useState(() => new Audio(audioData.url));
    const [playing, setPlaying] = useState(false);

    useEffect(() => {
        audio.currentTime = 0;
        if (playing) {
            audio.play().catch(() => setPlaying(false));
        } else {
            audio.pause();
        }
    }, [audio, playing]);

    useEffect(() => {
        const stop = () => setPlaying(false);
        audio.addEventListener('ended', stop);
        return () => {
            audio.removeEventListener('ended', stop);
            audio.pause();
        };
    }, [audio]);

    return (
        <div className="audio-row">
            <button
                type="button"
                className="icon-button audio-play"
                aria-label={playing ? "Stop" : "Play"}
                onClick={() => setPlaying(!playing)}
            >
                { playing ? <IconStop /> : <IconPlay /> }
            </button>
            <span className="audio-speaker">{ audioData.speaker }</span>
            { audioData.subtitle && <span className="audio-subtitle">{ audioData.subtitle }</span> }
        </div>
     );
}

export default ResultAudioRow;
