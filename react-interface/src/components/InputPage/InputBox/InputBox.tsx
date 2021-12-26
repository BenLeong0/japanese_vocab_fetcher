import React, { useState } from 'react';
import TextareaAutosize from 'react-textarea-autosize';

import FullResponseItem from '../../../types/FullResponseItem';
import QueryParams from '../../../types/QueryParams';

import HttpService from '../../core/HttpService';
import UtilsService from '../../core/UtilsService';

import './InputBox.css';

interface InputBoxProps {
    setWordList: (s: FullResponseItem[]) => void;
    setErrorOccurred: (x: boolean) => void;
}

const InputBox: React.FC<InputBoxProps> = ({ setWordList, setErrorOccurred }) => {
    const httpService = new HttpService();
    const utilsService = new UtilsService();

    const [text, setText] = useState<string>('');
    const [isLoading, setIsLoading] = useState<boolean>(false);

    const sendWords = async (event: React.FormEvent<HTMLButtonElement>) => {
        event.preventDefault();

        setIsLoading(true);
        setErrorOccurred(false);

        const words: string[] = utilsService.extractWordsFromInput(text);
        const queryParams: QueryParams = {
            words: JSON.stringify(words),
        };

        try {
            const resp = await httpService.makeGetRequest("/words", queryParams);
            setWordList(resp);
            console.log(resp);
        }
        catch (error) {
            setErrorOccurred(true);
            console.log(error);
        }
        finally {
            setIsLoading(false);
        }
    }

    const textArea = (
        <TextareaAutosize
            name="main-input"
            className="main-input"
            value={text}
            onChange={(e: any) => setText(e.target.value)}
        />
    );
    const wordsDisplay = (
        <div className="words-display vertical-separation-small">
            {utilsService.extractWordsFromInput(text).map((word) =>
                <div className="word-display">{word}</div>
            )}
        </div>
    );
    const submitButton = (
        <button
            className="button-primary vertical-separation-medium"
            type="submit"
            onClick={sendWords}
        >
            Submit
        </button>
    );

    const loadingSpinner = <div className="loader vertical-separation-large"></div>;

    return (
        isLoading ? loadingSpinner : <>{textArea}{wordsDisplay}{submitButton}</>
    );
}

export default InputBox;
