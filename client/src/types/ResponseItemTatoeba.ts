import APIErrorDict from "./ResponseError";
import Sentence from "./Sentence";

export interface TatoebaMainData {
    sentences: Sentence[];
}

export default interface ResponseItemTatoeba {
    success: boolean;
    error: APIErrorDict | null;
    main_data: TatoebaMainData;
}
