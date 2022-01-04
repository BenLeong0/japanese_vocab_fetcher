import React from 'react';

import { JishoExtraItem } from '../../../types/ResponseItemJisho';


interface ResultRelatedWordProps {
    relatedWord: JishoExtraItem;
}

const ResultRelatedWord: React.FC<ResultRelatedWordProps> = ({ relatedWord }) => {
    const { slug, japanese } = relatedWord;

    const url = `https://jisho.org/word/${slug}`;

    return (
        <div
            className="related-word"
            onClick={()=> window.open(url, "_blank")}
        >
            { japanese[0].word || japanese[0].reading }
        </div>
    );
}

export default ResultRelatedWord;
