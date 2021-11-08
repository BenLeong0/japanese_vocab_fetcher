import FailedResponseItem from "./FailedResponseItem";
import ResponseItemJisho from "./ResponseItemJisho";
import ResponseItemOJAD from "./ResponseItemOJAD";
import ResponseItemSuzuki from "./ResponseItemSuzuki";
import ResponseItemWadoku from "./ResponseItemWadoku";
import ResponseItemForvo from "./ResponseItemForvo";
import ResponseItemWanikani from "./ResponseItemWanikani";


export default interface FullResponseItem {
    word: string;
    jisho: ResponseItemJisho | FailedResponseItem;
    ojad: ResponseItemOJAD | FailedResponseItem;
    suzuki: ResponseItemSuzuki | FailedResponseItem;
    wadoku: ResponseItemWadoku | FailedResponseItem;
    forvo: ResponseItemForvo | FailedResponseItem;
    wanikani: ResponseItemWanikani | FailedResponseItem;
}
