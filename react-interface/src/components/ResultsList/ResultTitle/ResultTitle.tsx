import React from 'react';


interface ResultTitleProps {
    children: string;
}

const ResultTitle: React.FunctionComponent<ResultTitleProps> = ({ children }) => {
    return <div className="result-title">{ children }</div>;
}

export default ResultTitle;
