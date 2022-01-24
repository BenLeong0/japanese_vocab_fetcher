import APIErrorDict from "./ResponseError";

export interface JapanesePodAudio {
    url: string;
    writing: string;
    reading: string;
}

export interface JapanesePodMainData {
    audio: JapanesePodAudio[];
}

export default interface ResponseItemJapanesePod {
    success: boolean;
    error: APIErrorDict | null;
    main_data: JapanesePodMainData;
}
