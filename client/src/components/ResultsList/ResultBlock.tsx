import React, { useState } from 'react';
import ResultAudio from './ResultAudio/ResultAudio';
import ResultDefinitions from './ResultDefinitions/ResultDefinitions';
import ResultReadings from './ResultReadings/ResultReadings';
import ResultRelatedWords from './ResultRelatedWords/ResultRelatedWords';
import ResultSentences from './ResultSentences/ResultSentences';
import ResultTags from './ResultTags/ResultTags';
import ResultTitle from './ResultTitle/ResultTitle';

import FullResponseItem from '../../types/FullResponseItem';
import { JishoAPIItemSense } from '../../types/ResponseItemJisho';
import Sentence from '../../types/Sentence';

import UtilsService from '../core/UtilsService';

import './ResultBlock.css';


interface ResultProps {
    data: FullResponseItem;
}

const Result: React.FunctionComponent<ResultProps> = ({ data }) => {
    const utilsService = new UtilsService();

    const [isExpanded, setIsExpanded] = useState<boolean>(true);
    const toggleIsExpanded = () => setIsExpanded(!isExpanded);

    const getCopyWord = (): string => {
        const isSuruSense = (sense: JishoAPIItemSense) => sense.parts_of_speech.includes("Suru verb");
        const isSuruVerb = data.jisho.main_data.results.some(x => x.senses.some(isSuruSense));
        return isSuruVerb ? data.word + "（する）" : data.word;
    }

    const getMostTrustedAccent = (): string => {
        if (data.ojad.main_data.accent.length > 0) return data.ojad.main_data.accent[0];
        if (data.wadoku.main_data.accent.length > 0) return data.wadoku.main_data.accent[0];
        if (data.suzuki.main_data.accent.length > 0) return data.suzuki.main_data.accent[0];
        return "";
    }

    const getFilteredDefinitions = (): string => {
        if (data.jisho.main_data.results.length === 0) return "";
        const senses = data.jisho.main_data.results.map(result => result.senses).flat(2);
        if (senses.length === 1) {
            const dfn = senses[0].english_definitions;
            const formattedDfn = dfn.map(word => utilsService.capitaliseString(word));
            return formattedDfn.join(" ; ");
        }
        else {
            const dfns = senses.map(sense => sense.english_definitions.slice(0, 2));
            const formattedDfns = dfns.map(dfn => dfn.map(word => utilsService.capitaliseString(word)));
            return formattedDfns.map(dfn => dfn.join(" ; ")).join("  /  ");
        }
    }

    const getContextSentence = (): Sentence => {
        if (data.wanikani.main_data.sentences.length > 0) return data.wanikani.main_data.sentences[0];
        if (data.tatoeba.main_data.sentences.length > 0) return data.tatoeba.main_data.sentences[0];
        return { en: '', ja: '' };
    }

    const copyString: string = [
        getCopyWord(),
        getMostTrustedAccent(),
        getFilteredDefinitions(),
        getContextSentence().ja,
        getContextSentence().en,
    ].join("\t");

    return (
        <article className="result">
            <ResultTitle
                isExpanded={isExpanded}
                toggleIsExpanded={toggleIsExpanded}
                copyString={copyString}
            >{ data.word }</ResultTitle>
            { isExpanded &&
                <div className="result-body">
                    <div className="result-aside">
                        <ResultReadings data={data} />
                        <ResultTags data={data} />
                        <ResultAudio data={data} />
                        <ResultRelatedWords data={data} />
                    </div>
                    <div className="result-main">
                        <ResultDefinitions data={data} />
                        <ResultSentences data={data} />
                    </div>
                </div>
            }
        </article>
    );
}

export default Result;
