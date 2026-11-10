import ResponseItemJapanesePod from "./ResponseItemJapanesePod";
import ResponseItemJDict from "./ResponseItemJDict";
import ResponseItemJisho from "./ResponseItemJisho";
import ResponseItemOJAD from "./ResponseItemOJAD";
import ResponseItemSuzuki from "./ResponseItemSuzuki";
import ResponseItemWadoku from "./ResponseItemWadoku";
import ResponseItemForvo from "./ResponseItemForvo";
import ResponseItemTatoeba from "./ResponseItemTatoeba";
import ResponseItemWanikani from "./ResponseItemWanikani";


export default interface FullResponseItem {
    word: string;
    japanesepod: ResponseItemJapanesePod;
    jdict: ResponseItemJDict;
    jisho: ResponseItemJisho;
    ojad: ResponseItemOJAD;
    suzuki: ResponseItemSuzuki;
    wadoku: ResponseItemWadoku;
    forvo: ResponseItemForvo;
    tatoeba: ResponseItemTatoeba;
    wanikani: ResponseItemWanikani;
}
