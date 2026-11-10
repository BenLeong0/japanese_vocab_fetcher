import APIErrorDict from "./ResponseError";

export interface NHKMainData {
    accent: string[];
}

export default interface ResponseItemNHK {
    success: boolean;
    error: APIErrorDict | null;
    main_data: NHKMainData;
}
