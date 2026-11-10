import APIErrorDict from "./ResponseError";

export interface JDictSense {
    parts_of_speech: string[];
    tags: string[];
    definitions: string[];
}

export interface JDictEntry {
    writings: string[];
    readings: string[];
    is_common: boolean;
    senses: JDictSense[];
}

export interface JDictExtraItem {
    writings: string[];
    readings: string[];
}

export interface JDictMainData {
    results: JDictEntry[];
    extra: JDictExtraItem[];
}

export default interface ResponseItemJDict {
    success: boolean;
    error: APIErrorDict | null;
    main_data: JDictMainData;
}
