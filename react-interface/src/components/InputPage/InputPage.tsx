import React from 'react';

import './InputPage.css';

export interface InputPageProps {

}

const InputPage: React.FC<InputPageProps> = () => {
    return (
        <div className="input-page">
            <form>
                <textarea />
                <button type="submit">Submit</button>
            </form>
        </div>
    );
}

export default InputPage;
