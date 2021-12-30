import React, { useState } from 'react';
import InputBox from './InputBox/InputBox';

import FullResponseItem from '../../types/FullResponseItem';

import ErrorIcon from "../../assets/icons/icon_error.svg";
import './InputPage.css';


export interface InputPageProps {
    setWordList: (s: FullResponseItem[]) => void;
}

const InputPage: React.FC<InputPageProps> = ({ setWordList }) => {
    const [errorOccurred, setErrorOccurred] = useState<boolean>(false);

    const errorMessage = (
        <div className="error-message vertical-separation-large">
            <img src={ErrorIcon} alt="error icon" />
            An error occurred. Please try again
            <img src={ErrorIcon} alt="error icon" />
        </div>
    );

    return (
        <div className="input-page">
            <InputBox setWordList={setWordList} setErrorOccurred={setErrorOccurred}/>
            { errorOccurred ? errorMessage : <></> }
        </div>
    );
}

export default InputPage;
