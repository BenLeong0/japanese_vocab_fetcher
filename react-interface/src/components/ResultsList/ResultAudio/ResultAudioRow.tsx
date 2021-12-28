/* eslint-disable react-hooks/exhaustive-deps */
import React, { useState, useEffect } from 'react';

import ResultAudioRowData from '../../../types/ResultAudioRowData';

import IconPlayButton from '../../../assets/icons/icon_play_button.svg'
import IconStopButton from '../../../assets/icons/icon_stop_button.svg'


interface ResultAudioRowProps {
    audioData: ResultAudioRowData;
}

const ResultAudioRow: React.FC<ResultAudioRowProps> = ({ audioData }) => {
    const [audio] = useState(new Audio(audioData.url));
    const [playing, setPlaying] = useState(false);

    const togglePlaying = () => setPlaying(!playing);

    useEffect(() => {
        audio.currentTime = 0;
        playing ? audio.play() : audio.pause();
      },
      [playing]
    );

    useEffect(() => {
      audio.addEventListener('ended', () => setPlaying(false));
      return () => {
        audio.removeEventListener('ended', () => setPlaying(false));
      };
    }, []);

    return (
        <div className="result-audio">
            <img
                src={ playing ? IconStopButton : IconPlayButton }
                alt="audio player icon"
                className="audio-player"
                onClick={togglePlaying}
            />
            <div className="result-audio-speaker">{ audioData.speaker }</div>
            <div className="result-audio-subtitle">{ audioData.subtitle }</div>
        </div>
     );
}

export default ResultAudioRow;
