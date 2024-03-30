import APIErrorDict from "./ResponseError";
import Sentence from "./Sentence";

export interface TangorinMainData {
    sentences: Sentence[];
}

export default interface ResponseItemTangorin {
    success: boolean;
    error: APIErrorDict | null;
    main_data: TangorinMainData;
}
