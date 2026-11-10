import APIErrorDict from "./ResponseError";

export interface KanjiumMainData {
    accent: string[];
}

export default interface ResponseItemKanjium {
    success: boolean;
    error: APIErrorDict | null;
    main_data: KanjiumMainData;
}
