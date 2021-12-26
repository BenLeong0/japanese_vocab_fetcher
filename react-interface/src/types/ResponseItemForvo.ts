import APIErrorDict from "./ResponseError";

export interface ForvoAudio {
    url: string;
    username: string;
}

export interface ForvoMainData {
    audio: ForvoAudio[];
}

export default interface ResponseItemForvo {
    success: boolean;
    error: APIErrorDict | null;
    main_data: ForvoMainData;
}
