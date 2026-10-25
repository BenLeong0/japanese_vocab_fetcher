import React from 'react';

import { JDictEntry, JDictSense } from '../../../types/ResponseItemJDict';

import UtilsService from '../../core/UtilsService';


interface ResultJDictDefinitionProps {
    entry: JDictEntry;
}

const buildTitleText = (writing: string, reading: string): string => {
    return reading ? `${writing}【${reading}】` : writing;
}

const getWordType = (sense: JDictSense): string => {
    let wordType = sense.parts_of_speech.join("・");
    if (sense.tags.length > 0) {
        wordType += " (" + sense.tags.join(", ") + ")";
    }
    return wordType.trim();
}

const ResultJDictDefinition: React.FC<ResultJDictDefinitionProps> = ({ entry }) => {
    const utilsService = new UtilsService();

    const [mainWriting, ...otherWritings] = entry.writings;
    const [mainReading, ...otherReadings] = entry.readings;
    const otherForms = [
        ...otherWritings.map(writing => buildTitleText(writing, mainReading)),
        ...otherReadings.map(reading => buildTitleText(mainWriting || reading, mainWriting ? reading : "")),
    ];

    return (
        <div className="definition">
            <h4 className="definition-title ja">
                { mainWriting || mainReading }
                { mainWriting && mainReading &&
                    <span className="definition-reading">{ mainReading }</span>
                }
            </h4>
            <div className="senses">
                { entry.senses.map((sense, index) => {
                    const dfn = sense.definitions.map(utilsService.capitaliseString).join(" ; ");
                    return (
                        <div className="sense" key={index}>
                            { getWordType(sense) && <div className="sense-pos">{ getWordType(sense) }</div> }
                            <div className="sense-text">
                                <span
                                    className="sense-ordinal unselectable"
                                    title="Copy definition"
                                    onClick={() => utilsService.copyStringToClipboard(dfn)}
                                >{ index + 1 }.</span>
                                { dfn }
                            </div>
                        </div>
                    );
                })}
            </div>
            { otherForms.length > 0 &&
                <p className="other-forms">
                    Other forms: <span className="ja">{ otherForms.join("、") }</span>
                </p>
            }
        </div>
    );
}

export default ResultJDictDefinition;
