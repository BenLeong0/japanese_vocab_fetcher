import ResponseItemJisho from "./ResponseItemJisho";
import ResponseItemOJAD from "./ResponseItemOJAD";
import ResponseItemSuzuki from "./ResponseItemSuzuki";
import ResponseItemWadoku from "./ResponseItemWadoku";
import ResponseItemForvo from "./ResponseItemForvo";
import ResponseItemTangorin from "./ResponseItemTangorin";
import ResponseItemWanikani from "./ResponseItemWanikani";


export default interface FullResponseItem {
    word: string;
    jisho: ResponseItemJisho;
    ojad: ResponseItemOJAD;
    suzuki: ResponseItemSuzuki;
    wadoku: ResponseItemWadoku;
    forvo: ResponseItemForvo;
    tangorin: ResponseItemTangorin;
    wanikani: ResponseItemWanikani;
}
