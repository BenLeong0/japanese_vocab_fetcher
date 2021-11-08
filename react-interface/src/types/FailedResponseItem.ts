export interface APIErrorDict {
    error_msg: string;
    status_code: number;
    url: string;
}

export default interface FailedResponseItem {
    success: boolean;
    error: APIErrorDict;
}
