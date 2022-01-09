import React from 'react';
import ExpandButton from './ExpandButton';



interface FullExpandButtonProps {
    rowsDisplay: boolean;
    updateRowsDisplay: (x: boolean) => void;
}

const FullExpandButton: React.FC<FullExpandButtonProps> = ({ rowsDisplay, updateRowsDisplay }) => {
    const currentDisplay = () => rowsDisplay ? 1 : 0;
    const updateDisplay = (x: number) => {
        updateRowsDisplay(x === 1 ? true : false);
    }

    return <ExpandButton
        updateDisplay={updateDisplay}
        minDisplay={0}
        maxDisplay={1}
        batchSize={1}
        currentDisplay={currentDisplay()}
    />;
}

export default FullExpandButton;
