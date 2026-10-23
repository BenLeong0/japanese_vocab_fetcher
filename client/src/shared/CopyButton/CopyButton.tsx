import React, { useEffect, useState } from 'react';
import { IconCheck, IconCopy } from '../Icons/Icons';

import UtilsService from '../../components/core/UtilsService';


interface CopyButtonProps {
    text: string;
    label: string;
    className?: string;
}

const CopyButton: React.FC<CopyButtonProps> = ({ text, label, className }) => {
    const [copied, setCopied] = useState<boolean>(false);

    useEffect(() => {
        if (!copied) return;
        const timer = setTimeout(() => setCopied(false), 1200);
        return () => clearTimeout(timer);
    }, [copied]);

    const copy = () => {
        new UtilsService().copyStringToClipboard(text);
        setCopied(true);
    }

    return (
        <button
            type="button"
            className={`icon-button ${className || ""}`}
            title={label}
            aria-label={label}
            onClick={copy}
        >
            {copied ? <IconCheck /> : <IconCopy />}
        </button>
    );
}

export default CopyButton;
