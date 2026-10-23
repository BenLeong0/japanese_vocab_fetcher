import React from 'react';

import './Section.css';


interface SectionProps {
    title: string;
    className?: string;
    children: React.ReactNode;
}

const Section: React.FC<SectionProps> = ({ title, className, children }) => {
    return (
        <section className={`section ${className || ""}`}>
            <h3 className="section-title">{title}</h3>
            {children}
        </section>
    );
}

export default Section;
