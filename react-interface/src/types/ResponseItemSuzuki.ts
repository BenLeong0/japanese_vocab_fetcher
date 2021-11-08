export interface SuzukiMainData {
    accent: string[];
}

export default interface ResponseItemSuzuki {
    main_data: SuzukiMainData;
    success: boolean;
}
