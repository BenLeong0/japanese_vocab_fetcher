export interface OJADMainData {
    accent: string[];
}

export default interface ResponseItemOJAD {
    main_data: OJADMainData;
    success: boolean;
}
