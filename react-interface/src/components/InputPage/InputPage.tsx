import React, { useState } from 'react';
import TextareaAutosize from 'react-textarea-autosize';

import QueryParams from '../../types/QueryParams';
import HttpService from '../core/HttpService';

import './InputPage.css';

export interface InputPageProps {

}

const InputPage: React.FC<InputPageProps> = () => {
    const httpService = new HttpService();
    const [text, setText] = useState<string>('');

    const sendWords = async (event: React.FormEvent<HTMLButtonElement>) => {
        event.preventDefault()

        const words: string[] = getWords(text);
        const wordsString: string = JSON.stringify(words);

        const queryParams: QueryParams = {
            words: wordsString,
        };
        httpService.makeGetRequest("/words", queryParams);
    }

    return (
        <div className="input-page">
            <TextareaAutosize
                name="main-input"
                className="main-input"
                value={text}
                onChange={(e) => setText(e.target.value)}
            />
            <div className="words-display">
                {getWords(text).map((word) =>
                    <div className="word-display">{word}</div>
                )}
            </div>
            <button className="button-primary" type="submit" onClick={sendWords}>Submit</button>
        </div>
    );
}

export const getWords = (s: string): string[] => {
    return s.split(/\s+/).filter(char => char !== "");
}

export default InputPage;
