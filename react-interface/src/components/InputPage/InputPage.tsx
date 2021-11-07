import React, { useState } from 'react';
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

        const queryParams = {
            words: wordsString,
        };
        httpService.makeGetRequest('', queryParams);
    }

    return (
        <div className="input-page">
            <input
                value={text}
                onChange={(e) => setText(e.target.value)}
            />
            <button className="button-primary" type="submit" onClick={sendWords}>Submit</button>
        </div>
    );
}

export const getWords = (s: string): string[] => {
    return s.split(/\s+/).filter(char => char !== "");
}

export default InputPage;
