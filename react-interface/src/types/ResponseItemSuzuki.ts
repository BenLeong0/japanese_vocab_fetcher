import APIErrorDict from "./ResponseError";

export interface SuzukiMainData {
    accent: string[];
}

export default interface ResponseItemSuzuki {
    success: boolean;
    error: APIErrorDict | null;
    main_data: SuzukiMainData;
}
