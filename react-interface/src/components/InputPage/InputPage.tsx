import React, { useState } from 'react';
import HttpService from '../core/HttpService';

import './InputPage.css';

export interface InputPageProps {

}

const InputPage: React.FC<InputPageProps> = () => {
    const httpService = new HttpService();
    const [text, setText] = useState<string>('');

    const getWords = (): string[] => {
        return text.split('\n').filter(word => word.trim().length > 0);
    }

    const sendWords = async (event: React.FormEvent<HTMLButtonElement>) => {
        event.preventDefault()

        const words: string[] = getWords();
        const wordsString: string = JSON.stringify(words);

        const queryParams = {
            words: wordsString,
        };
        httpService.makeGetRequest('', queryParams);
    }

    return (
        <div className="input-page">
            <textarea
                value={text}
                onChange={(e) => setText(e.target.value)}
            />
            <button className="button-primary" type="submit" onClick={sendWords}>Submit</button>
        </div>
    );
}

export default InputPage;
