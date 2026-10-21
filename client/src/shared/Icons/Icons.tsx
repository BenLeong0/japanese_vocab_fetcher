import React from 'react';


interface IconProps {
    className?: string;
}

const base = {
    width: 24,
    height: 24,
    viewBox: "0 0 24 24",
    fill: "none",
    stroke: "currentColor",
    strokeWidth: 2,
    strokeLinecap: "round" as const,
    strokeLinejoin: "round" as const,
    "aria-hidden": true,
};

export const IconCopy: React.FC<IconProps> = ({ className }) => (
    <svg {...base} className={className}>
        <rect x="9" y="9" width="12" height="12" rx="2" />
        <path d="M5 15H4a1 1 0 0 1-1-1V4a1 1 0 0 1 1-1h10a1 1 0 0 1 1 1v1" />
    </svg>
);

export const IconCheck: React.FC<IconProps> = ({ className }) => (
    <svg {...base} className={className}>
        <path d="M5 12.5l4.5 4.5L19 7" />
    </svg>
);

export const IconChevron: React.FC<IconProps & { up?: boolean }> = ({ className, up }) => (
    <svg {...base} className={className}>
        {up ? <path d="M6 15l6-6 6 6" /> : <path d="M6 9l6 6 6-6" />}
    </svg>
);

export const IconPlay: React.FC<IconProps> = ({ className }) => (
    <svg {...base} className={className} fill="currentColor" stroke="none">
        <path d="M8 5.5v13l10-6.5z" />
    </svg>
);

export const IconStop: React.FC<IconProps> = ({ className }) => (
    <svg {...base} className={className} fill="currentColor" stroke="none">
        <rect x="7" y="7" width="10" height="10" rx="1.5" />
    </svg>
);

export const IconAlert: React.FC<IconProps> = ({ className }) => (
    <svg {...base} className={className}>
        <circle cx="12" cy="12" r="9" />
        <path d="M12 8v4.5M12 16h.01" />
    </svg>
);
