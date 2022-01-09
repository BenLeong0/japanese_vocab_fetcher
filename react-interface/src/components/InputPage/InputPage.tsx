import React, { useState } from 'react';
import ErrorMessage from '../../shared/ErrorMessage/ErrorMessage';
import InputBox from './InputBox/InputBox';

import FullResponseItem from '../../types/FullResponseItem';

import './InputPage.css';


export interface InputPageProps {
    setWordList: (s: FullResponseItem[]) => void;
}

const InputPage: React.FC<InputPageProps> = ({ setWordList }) => {
    const [errorOccurred, setErrorOccurred] = useState<boolean>(false);

    return (
        <div className="input-page">
            <InputBox setWordList={setWordList} setErrorOccurred={setErrorOccurred}/>
            { errorOccurred && <ErrorMessage>An error occurred. Please try again</ErrorMessage> }
        </div>
    );
}

export default InputPage;
