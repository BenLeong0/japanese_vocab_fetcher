import React from 'react';
import { IconAlert } from '../Icons/Icons';

import './ErrorMessage.css';


interface ErrorMessageProps {
    children: string;
}

const ErrorMessage: React.FunctionComponent<ErrorMessageProps> = ({ children }) => {
    return (
        <div className="error-message" role="alert">
            <IconAlert className="error-message-icon" />
            { children }
        </div>
    );
}

export default ErrorMessage;
