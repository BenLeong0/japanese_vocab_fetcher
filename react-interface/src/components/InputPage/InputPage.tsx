import React, { useState } from 'react';
import TextareaAutosize from 'react-textarea-autosize';
import FullResponseItem from '../../types/FullResponseItem';

import QueryParams from '../../types/QueryParams';
import HttpService from '../core/HttpService';

import ErrorIcon from "../../assets/icons/icon_error.svg";
import './InputPage.css';


export interface InputPageProps {
    setWordList: (s: FullResponseItem[]) => void;
}

const InputPage: React.FC<InputPageProps> = ({ setWordList }) => {
    const httpService = new HttpService();

    const [text, setText] = useState<string>('');
    const [isLoading, setIsLoading] = useState<boolean>(false);
    const [errorOccurred, setErrorOccurred] = useState<boolean>(false);

    const sendWords = async (event: React.FormEvent<HTMLButtonElement>) => {
        event.preventDefault();
        setIsLoading(true);
        setErrorOccurred(false);

        const words: string[] = getWords(text);
        const wordsString: string = JSON.stringify(words);

        const queryParams: QueryParams = {
            words: wordsString,
        };

        try {
            const resp = await httpService.makeGetRequest("/worsdfds", queryParams);
            console.log(resp);
            setWordList(resp);
        }
        catch (error) {
            console.log(error);
            setErrorOccurred(true);
        }
        setIsLoading(false);
    }

    const errorMessageDisplay = () => {
        return (
            errorOccurred ?
            <div className="error-message vertical-separation-large">
                <img src={ErrorIcon} alt="error icon" />
                An error occurred. Please try again
                <img src={ErrorIcon} alt="error icon" />
            </div> :
            <></>
        );
    }
    const getInputBox = () => {
        if (isLoading) {
            return <div className="loader vertical-separation-large"></div>;
        }
        return (
            <>
                <TextareaAutosize
                    name="main-input"
                    className="main-input"
                    value={text}
                    onChange={(e) => setText(e.target.value)}
                />
                <div className="words-display vertical-separation-small">
                    {getWords(text).map((word) =>
                        <div className="word-display">{word}</div>
                    )}
                </div>
                <button
                    className="button-primary vertical-separation-medium"
                    type="submit"
                    onClick={sendWords}
                >Submit</button>
            </>
        );
    }

    return (
        <div className="input-page">
            { getInputBox() }
            { errorMessageDisplay() }
        </div>
    );
}

export const getWords = (s: string): string[] => {
    return s.split(/\s+/).filter(char => char !== "");
}

export default InputPage;
