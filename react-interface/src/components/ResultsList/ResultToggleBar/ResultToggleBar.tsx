import React from 'react';

import IconChevronUp from '../../../assets/icons/icon_chevron_up.svg';
import IconChevronDown from '../../../assets/icons/icon_chevron_down.svg';
import './ResultToggleBar.css';


interface ResultToggleBarProps {
    isExpanded: boolean;
    toggleIsExpanded: () => void;
}

const ResultToggleBar: React.FC<ResultToggleBarProps> = ({ isExpanded, toggleIsExpanded }) => {
    const imgSrc = isExpanded ? IconChevronUp : IconChevronDown;

    return (
        <div
            className="result-toggle-bar"
            onClick={toggleIsExpanded}
        >
            <img src={imgSrc} alt="chevron to expand or collapse the result"/>
        </div>
     );
}

export default ResultToggleBar;
