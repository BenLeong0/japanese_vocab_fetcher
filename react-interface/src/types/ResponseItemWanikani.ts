import APIErrorDict from "./ResponseError";

export interface WanikaniContextSentence {
    en: string;
    ja: string;
}

export interface WanikaniPronunciationAudioMetadata {
    gender: string;
    source_id: number;
    pronunciation: string;
    voice_actor_id: number;
    voice_actor_name: string;
    voice_description: string;
}

export interface WanikaniPronunciationAudio {
    url: string;
    content_type: string;
    metadata: WanikaniPronunciationAudioMetadata;
}

export interface WanikaniMainData {
    audio: WanikaniPronunciationAudio[];
    sentences: WanikaniContextSentence[];
}

export default interface ResponseItemWanikani {
    success: boolean;
    error: APIErrorDict | null;
    main_data: WanikaniMainData;
}
