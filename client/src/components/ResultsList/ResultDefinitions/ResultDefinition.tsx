import React from 'react';
import ResultDefinitionSense from './ResultDefinitionSense';

import { JishoAPIItem, JishoAPIItemJapanese } from '../../../types/ResponseItemJisho';


interface ResultDefinitionProps {
    definitionData: JishoAPIItem;
}

const buildTitleText = (word: JishoAPIItemJapanese): string => {
    const main = word.word || word.reading || "";
    const subtext = (word.word && word.reading) ? `【${word.reading}】` : "";
    return main + subtext;
}

const ResultDefinition: React.FC<ResultDefinitionProps> = ({ definitionData }) => {
    const [mainForm, ...otherForms] = definitionData.japanese;

    return (
        <div className="definition">
            <h4 className="definition-title ja">
                { mainForm.word || mainForm.reading }
                { mainForm.word && mainForm.reading &&
                    <span className="definition-reading">{ mainForm.reading }</span>
                }
            </h4>
            <div className="senses">
                { definitionData.senses.map((sense, index) =>
                    <ResultDefinitionSense key={index} ordinality={index+1} sense={sense} />
                )}
            </div>
            { otherForms.length > 0 &&
                <p className="other-forms">
                    Other forms: <span className="ja">{ otherForms.map(buildTitleText).join("、") }</span>
                </p>
            }
        </div>
    );
}

export default ResultDefinition;
