import React from 'react';

import { JishoExtraItem } from '../../../types/ResponseItemJisho';


interface ResultRelatedWordProps {
    relatedWord: JishoExtraItem;
}

const ResultRelatedWord: React.FC<ResultRelatedWordProps> = ({ relatedWord }) => {
    const { slug, japanese } = relatedWord;
    const url = `https://jisho.org/word/${slug}`;

    return (
        <a
            className="chip chip-link ja"
            href={url}
            target="_blank"
            rel="noopener noreferrer"
        >
            { japanese[0].word || japanese[0].reading }
        </a>
    );
}

export default ResultRelatedWord;
