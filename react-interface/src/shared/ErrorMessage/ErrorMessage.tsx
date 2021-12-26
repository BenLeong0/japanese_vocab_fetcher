import React from 'react';

import ErrorIcon from "../../assets/icons/icon_error.svg";
import './ErrorMessage.css';


interface ErrorMessageProps {
    children: string;
}

const ErrorMessage: React.FunctionComponent<ErrorMessageProps> = ({ children }) => {
    return (
        <div className="error-message vertical-separation-large">
            <img src={ErrorIcon} alt="error icon" />
            { children }
            <img src={ErrorIcon} alt="error icon" />
        </div>
    );
}

export default ErrorMessage;
