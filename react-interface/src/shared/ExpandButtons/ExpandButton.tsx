import React from 'react';

import IconPlus from '../../assets/icons/icon_plus.svg'
import IconMinus from '../../assets/icons/icon_minus.svg'

import './ExpandButton.css'


interface ExpandButtonProps {
    currentDisplay: number;
    updateDisplay: (newDisplay: number) => void;
    maxDisplay: number;
    minDisplay: number;
    batchSize: number;
}

const ExpandButton: React.FC<ExpandButtonProps> = ({
    currentDisplay,
    updateDisplay,
    maxDisplay,
    minDisplay,
    batchSize
}) => {
    const displayPlus = () => currentDisplay < maxDisplay;
    const pressPlus = () => updateDisplay(Math.min(maxDisplay, currentDisplay + batchSize));
    const displayMinus = () => currentDisplay > minDisplay;
    const pressMinus = () => updateDisplay(Math.max(minDisplay, currentDisplay - batchSize));

    return (
        <div className="flex-row">
            { displayMinus() &&
                <div className="expand-button expand-button-decrease" onClick={pressMinus}>
                    <img src={IconMinus} alt="button to decrease the number of items displayed" />
                </div>
            }
            { displayPlus() &&
                <div className="expand-button expand-button-increase" onClick={pressPlus}>
                    <img src={IconPlus} alt="button to increase the number of items displayed" />
                </div>
            }
        </div>
    );
}

export default ExpandButton;
