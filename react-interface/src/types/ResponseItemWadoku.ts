export interface WadokuMainData {
    accent: string[];
}

export default interface ResponseItemWadoku {
    main_data: WadokuMainData;
    success: boolean;
}
