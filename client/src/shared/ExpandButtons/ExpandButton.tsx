import React from 'react';


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
    const canShowMore = currentDisplay < maxDisplay;
    const canShowLess = currentDisplay > minDisplay;
    const showMore = () => updateDisplay(Math.min(maxDisplay, currentDisplay + batchSize));
    const showLess = () => updateDisplay(Math.max(minDisplay, currentDisplay - batchSize));

    if (!canShowMore && !canShowLess) return null;

    return (
        <div className="expand-buttons">
            { canShowMore &&
                <button type="button" className="text-button" onClick={showMore}>
                    Show more
                </button>
            }
            { canShowLess &&
                <button type="button" className="text-button" onClick={showLess}>
                    Show less
                </button>
            }
        </div>
    );
}

export default ExpandButton;
