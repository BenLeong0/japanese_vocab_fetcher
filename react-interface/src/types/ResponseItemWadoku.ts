import APIErrorDict from "./ResponseError";

export interface WadokuMainData {
    accent: string[];
}

export default interface ResponseItemWadoku {
    success: boolean;
    error: APIErrorDict | null;
    main_data: WadokuMainData;
}
