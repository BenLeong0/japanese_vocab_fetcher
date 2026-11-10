import ResponseItemJapanesePod from "./ResponseItemJapanesePod";
import ResponseItemJDict from "./ResponseItemJDict";
import ResponseItemJisho from "./ResponseItemJisho";
import ResponseItemNHK from "./ResponseItemNHK";
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
    nhk: ResponseItemNHK;
    ojad: ResponseItemOJAD;
    suzuki: ResponseItemSuzuki;
    wadoku: ResponseItemWadoku;
    forvo: ResponseItemForvo;
    tatoeba: ResponseItemTatoeba;
    wanikani: ResponseItemWanikani;
}
