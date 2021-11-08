export interface ForvoAudio {
    url: string;
    username: string;
}

export interface ForvoMainData {
    audio: ForvoAudio[];
}

export default interface ResponseItemForvo {
    main_data: ForvoMainData;
    success: boolean;
}
