import APIErrorDict from "./ResponseError";

export interface OJADMainData {
    accent: string[];
}

export default interface ResponseItemOJAD {
    success: boolean;
    error: APIErrorDict | null;
    main_data: OJADMainData;
}
